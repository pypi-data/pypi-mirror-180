from pathlib import Path
import json
import yaml
import shutil
import subprocess
import inquirer
import sys
from datetime import datetime
import os
import click
from .odoo_config import current_version
from .odoo_config import MANIFEST
from .tools import _is_dirty
from .odoo_config import customs_dir
from .cli import cli, pass_config, Commands
from .lib_clickhelpers import AliasedGroup
from .tools import split_hub_url
from .tools import autocleanpaper
from .tools import copy_dir_contents, rsync
from .tools import abort
from .tools import __assure_gitignore
from .tools import _write_file

ADDONS_OCA = "addons_OCA"


@cli.group(cls=AliasedGroup)
@pass_config
def src(config):
    pass


def _turn_into_odoosh(ctx, path):
    content = MANIFEST()
    odoosh_path = Path(os.environ["ODOOSH_REPO"] or "../odoo.sh").resolve().absolute()
    if not odoosh_path.exists():
        subprocess.check_call(
            [
                "git",
                "clone",
                "https://github.com/Odoo-Ninjas/odoo.sh.git",
                odoosh_path,
            ]
        )
        subprocess.check_call(
            [
                "gimera",
                "apply",
            ],
            cwd=odoosh_path.absolute(),
        )
    content["auto_repo"] = 1  # for OCA modules
    content = yaml.safe_load((path / "gimera.yml").read_text())
    include = []
    file_changed = False
    for subdir in ["odoo", "enterprise"]:
        if (path / subdir).is_dir() and not (path / subdir).is_symlink():
            shutil.rmtree(path / subdir)
        content["repos"] = [x for x in content["repos"] if x["path"] != subdir]
        include.append(
            (str(odoosh_path / subdir / str(current_version())), str(subdir))
        )

    if _write_file(path / ".include_wodoo", json.dumps(include)):
        ctx.invoke(clear_cache)
    __assure_gitignore(path / ".gitignore", ".include_wodoo")

    (path / "gimera.yml").write_text(yaml.dump(content, default_flow_style=False))
    click.secho("Please reload now!", fg="yellow")
    Commands.invoke(ctx, "reload", no_auto_repo=True)
    _identify_duplicate_modules()


@src.command(name="init", help="Create a new odoo")
@click.argument("path", required=True)
@click.option("--odoosh", is_flag=True)
@click.pass_context
@pass_config
def init(config, ctx, path, odoosh):
    from .module_tools import make_customs

    path = Path(path)
    if not path.exists():
        path.mkdir(parents=True)
    make_customs(path)

    odoosh and _turn_into_odoosh(ctx, Path(os.getcwd()))


@src.command(help="Makes odoo and enterprise code available from common code")
@click.pass_context
@pass_config
def make_odoo_sh_compatible(config, ctx):
    _turn_into_odoosh(ctx, customs_dir())


@src.command()
@pass_config
@click.option("-n", "--name", required=True)
@click.option("-p", "--parent-path", required=False)
def make_module(config, name, parent_path):
    cwd = parent_path or config.working_dir
    from .module_tools import make_module as _tools_make_module

    _tools_make_module(
        cwd,
        name,
    )


@src.command(name="update-ast")
@click.option("-f", "--filename", required=False)
def update_ast(filename):
    from .odoo_parser import update_cache

    started = datetime.now()
    click.echo("Updating ast - can take about one minute")
    update_cache(filename or None)
    click.echo(
        "Updated ast - took {} seconds".format((datetime.now() - started).seconds)
    )


@src.command("goto-inherited")
@click.option("-f", "--filepath", required=True)
@click.option("-l", "--lineno", required=True)
def goto_inherited(filepath, lineno):
    from .odoo_parser import goto_inherited_view

    lineno = int(lineno)
    filepath = customs_dir() / filepath
    lines = filepath.read_text().split("\n")
    filepath, lineno = goto_inherited_view(filepath, lineno, lines)
    if filepath:
        print(f"FILEPATH:{filepath}:{lineno}")


@src.command(name="show-addons-paths")
def show_addons_paths():
    from .odoo_config import get_odoo_addons_paths

    paths = get_odoo_addons_paths(relative=True)
    for path in paths:
        click.echo(path)


@src.command(name="make-modules", help="Puts all modules in /modules.txt")
@pass_config
def make_modules(config):
    modules = ",".join(MANIFEST()["install"])
    (config.dirs["customs"] / "modules.txt").write_text(modules)
    click.secho(f"Updated /modules.txt with: \n\n", fg="yellow")
    click.secho(modules)


@src.command()
@pass_config
def setup_venv(config):
    dir = customs_dir()
    os.chdir(dir)
    venv_dir = dir / ".venv"
    gitignore = dir / ".gitignore"
    if ".venv" not in gitignore.read_text().split("\n"):
        with gitignore.open("a") as f:
            f.write("\n.venv\n")

    subprocess.check_call(["python3", "-m", "venv", venv_dir.absolute()])

    click.secho("Please execute following commands in your shell:", bold=True)
    click.secho("source '{}'".format(venv_dir / "bin" / "activate"))
    click.secho("pip3 install cython")
    click.secho(
        "pip3 install -r https://raw.githubusercontent.com/odoo/odoo/{}/requirements.txt".format(
            current_version()
        )
    )
    requirements1 = (
        Path(__file__).parent.parent
        / "images"
        / "odoo"
        / "config"
        / str(current_version())
        / "requirements.txt"
    )
    click.secho("pip3 install -r {}".format(requirements1))


def try_to_get_module_from_oca(modulename):
    from .odoo_config import current_version, customs_dir

    ocapath = Path(os.environ["ODOOSH_REPO"]) / "OCA"
    if not ocapath.exists():
        abort(f"Not found: {ocapath}")
    version = str(current_version())

    for match in ocapath.rglob(modulename):
        if not match.is_dir():
            continue
        if not (match / "__manifest__.py").exists():
            continue
        if match.parent.name != version:
            continue
        return match
    raise KeyError(modulename)


@src.command()
@pass_config
def fetch_modules(config):
    _fetch_modules(config)


def _fetch_modules(config):
    """
    if MANIFEST['auto_repo'] then try to get oca repos from the
    ninja odoo.sh
    """
    manifest = MANIFEST()
    if not manifest.get("auto_repo", False):
        return

    from .tools import rsync
    from .odoo_config import customs_dir
    from .module_tools import Modules, Module
    from .lib_src import try_to_get_module_from_oca

    modules = Modules()
    for module in manifest.get("install", []):
        try:
            mod = Module.get_by_name(module)
        except KeyError:
            oca_module = try_to_get_module_from_oca(module)
            destination = customs_dir() / ADDONS_OCA / module
            if not destination.parent.exists():
                destination.mkdir(exist_ok=True, parents=True)
            rsync(oca_module, destination)
    addons_paths = manifest.get("addons_paths", [])
    if not [x for x in addons_paths if x == ADDONS_OCA]:
        addons_paths.append(ADDONS_OCA)
    manifest["addons_paths"] = addons_paths
    manifest.rewrite()

    _identify_duplicate_modules()


def _identify_duplicate_modules():
    # remove duplicate modules or at least identify them:
    from .module_tools import Modules, Module

    modules = Modules()
    all_modules = modules.get_all_modules_installed_by_manifest()
    for x in all_modules:
        for y in customs_dir().rglob(x):
            if not y.is_dir():
                continue
            if not (y / "__manifest__.py").exists():
                continue
            module = Module.get_by_name(x)
            if y.resolve().absolute() != module.path.resolve().absolute():
                abort(
                    "Found duplicate module, which is a problem for odoo.sh deployment.\n"
                    "Not clear which module gets installed: \n"
                    f"{module.path}\n"
                    f"{y}"
                )


@src.command
@pass_config
def clear_cache(config):
    from .module_tools import ModulesCache

    ModulesCache._clear_cache()


@src.command
@click.option("-f", "--fix-not-in-manifest", is_flag=True)
@pass_config
def show_installed_modules(config, fix_not_in_manifest):
    from .module_tools import DBModules, Module
    from .odoo_config import customs_dir
    path = customs_dir()
    collected = []
    not_in_manifest = []
    manifest = MANIFEST()
    setinstall = manifest.get('install', [])

    for module in sorted(DBModules.get_all_installed_modules()):
        try:
            mod = Module.get_by_name(module)
            click.secho(f"{module}: {mod.path}", fg='green')
            if not [x for x in setinstall if x == module]:
                not_in_manifest.append(module)
        except KeyError:
            collected.append(module)

    for module in not_in_manifest:
        if fix_not_in_manifest:
            setinstall += [module]
            click.secho(f"Added to manifest: {module}", fg='green')
        else:
            click.secho(f"Not in MANIFEST: {module}", fg='yellow')
    for module in collected:
        click.secho(f"Not in filesystem: {module}", fg='red')

    if fix_not_in_manifest:
        manifest['install'] = setinstall
        manifest.rewrite()


Commands.register(clear_cache)
