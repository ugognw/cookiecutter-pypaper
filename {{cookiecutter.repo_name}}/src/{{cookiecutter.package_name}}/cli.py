"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m{{cookiecutter.package_name}}` python will execute
    ``__main__.py`` as a script. That means there will not be any
    ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there"s no ``{{cookiecutter.package_name}}.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
{%- if cookiecutter.command_line_interface == "click" %}
import click
{%- elif cookiecutter.command_line_interface == "argparse" %}
import argparse
{%- elif cookiecutter.command_line_interface == "fire" %}
import fire
{%- elif cookiecutter.command_line_interface == "typer" %}
from typing import Annotated

from rich.console import Console
from typer import Argument, Typer
{%- else %}
import sys
{%- endif %}

import {{ cookiecutter.package_name }}
{%- if cookiecutter.command_line_interface == "click" %}


@click.command(name='{{ cookiecutter.cli_bin_name }}'x)
@click.option(
    '-v',
    '--version',
    is_flag=True,
    default=False,
    help='Show the version and exit.',
)
def main(version):
    if version:
        click.echo(f"{{ cookiecutter.cli_bin_name }}-{{ '{' }}{{ cookiecutter.cli_bin_name }}.__version__{{ '}' }}")
{%- elif cookiecutter.command_line_interface == "argparse" %}


parser = argparse.ArgumentParser(description="Command description.")
parser.add_argument(
    "names",
    metavar="NAME",
    nargs=argparse.ZERO_OR_MORE,
    help="A name of something.",
)


def main(args=None):
    args = parser.parse_args(args=args)
    print(args.names)
{%- elif cookiecutter.command_line_interface == "fire" %}


def help():
    print("{{ cookiecutter.cli_bin_name }}")
    print("=" * len("{{ cookiecutter.cli_bin_name }}"))
    print("{{ cookiecutter.project_short_description }}")

def main():
    fire.Fire({
        "help": help
    })
{%- elif cookiecutter.command_line_interface == "typer" %}


app = Typer(add_completion=False)


@app.command()
def main(n: Annotated[int, Argument(min=0, help="{{ cookiecutter.project_short_description }}")]) -> None:
    """{{ cookiecutter.project_short_description }}"""

    Console().print(f'{{ cookiecutter.cli_bin_name }}-{{ "{" }}{{ cookiecutter.cli_bin_name }}.__version__{{ "}" }}')
{%- else %}


def main(argv=sys.argv):
    """
    Args:
        argv (list): List of arguments

    Returns:
        int: A return code

    Does stuff.
    """
    print(argv)
    return 0
{%- endif %}
