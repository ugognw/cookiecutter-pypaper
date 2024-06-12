import pathlib
import shutil
import subprocess
import sys


try:
    from click.termui import secho
except ImportError:
    warn = note = success = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)

    def success(text):
        for line in text.splitlines():
            secho(line, fg="green", bold=True)


if __name__ == "__main__":
    cwd = pathlib.Path().resolve()
    src = cwd / 'src'

{%- if cookiecutter.command_line_interface == 'no' %}
    src.joinpath('{{ cookiecutter.package_name }}', '__main__.py').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', 'cli.py').unlink()
{% endif %}

{%- if cookiecutter.license == "no" %}
    cwd.joinpath('LICENSE').unlink()
{%- endif %}

{%- if cookiecutter.support_type_checking == "no" %}
    cwd.joinpath('src', '{{ cookiecutter.package_name }}', 'py.typed').unlink()
{%- endif %}

    width = min(140, shutil.get_terminal_size(fallback=(140, 0)).columns)
{%- if cookiecutter.initialize_git_repository == 'yes' %}
    note(' Initializing Git repository '.center(width, "#"))
    try:
        _ = subprocess.check_call(['git', 'init'])
        _ = subprocess.check_call(['git', 'add', '--all'])
        _ = subprocess.check_call(['git', 'commit', '-m', '"Add initial project skeleton."'])
        _ = subprocess.check_call(['git', 'tag', 'v{{ cookiecutter.version }}'])
        _ = subprocess.check_call(['git', 'remote', 'add', 'origin', 'git@{{ cookiecutter.__repo_url }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git'])
        _ = subprocess.check_call(['git', 'push', '-u', 'origin', '{{ cookiecutter.repo_main_branch }}'])
        _ = subprocess.check_call(['git', 'push', '-u', 'origin', 'v{{ cookiecutter.version }}'])
    except subprocess.CalledProcessError as err:
        print(err.args)
{%- endif %}
    package_installed = False
{% if cookiecutter.install_package == 'yes' %}
    note(' Installing package and dependencies '.center(width, "#"))
    try:
        _ = subprocess.check_call(['hatch', 'env', 'create', 'default'])
        package_installed = True
    except FileNotFoundError as err:
        print(err.args)
        note('Installing hatch'.center(width, "#"))
        p = subprocess.run(
            [
                '/usr/bin/env',
                'brew',
                'install',
                'hatch',
            ],
        )
        note('Hatch successfully installed'.center(width, "#"))
        _ = subprocess.check_call(['hatch', 'env', 'create', 'default'])
        package_installed = True
    except subprocess.CalledProcessError as err:
        print(err.args)
    except Exception:
        print(err.args)
        warn(
            'Unable to install Hatch.'.center(width, "#")
        )
        warn(
            'You will need to install Hatch in order to install the project and activate the virtual environment.'.center(width, "#")
        )
        warn(
            'https://hatch.pypa.io/latest/install/.'.center(width, "#")
        )
{%- endif %}

    pre_commit_installed = False
{%- if cookiecutter.pre_commit == 'no' %}
    cwd.joinpath('.pre-commit-config.yaml').unlink()
{%- elif cookiecutter.install_precommit_hooks == 'yes' %}
    note(' Setting up pre-commit '.center(width, "#"))
    if cwd.joinpath('.git').exists():
        try:
            _ = subprocess.check_call(['hatch', 'run', 'pre-commit', 'install', '--install-hooks'])
            _ = subprocess.check_call(['hatch', 'run', 'pre-commit', 'autoupdate'])
            pre_commit_installed = True
        except subprocess.CalledProcessError:
            try:
                _ = subprocess.check_call(['hatch', 'run', 'pip', 'install', 'pre-commit'])
                _ = subprocess.check_call(['hatch', 'run', 'pre-commit', 'autoupdate'])
            except subprocess.CalledProcessError:
                warn(
                'Unable to install pre-commit.'.center(width, "#")
                )

    else:
        print('Skipping precommit install.')
{%- endif %}

    success(' Successfully created `{{ cookiecutter.repo_name }}` '.center(width, "#"))
    print('See .cookiecutterrc for instructions on regenerating the project.')
    note('To get started run these:')
    commands = [
        'cd {{ cookiecutter.repo_name }}',
{%- if cookiecutter.initialize_git_repository == 'no' %}
        'git init',
{%- endif %}
    ]

{%- if cookiecutter.initialize_git_repository == 'no' %}
    commands.extend(
        (
            'git add --all',
            'git commit -m "Add initial project skeleton."',
            'git tag v{{ cookiecutter.version }}',
            'git remote add origin git@github.com:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git',
            'git push -u origin {{ cookiecutter.repo_main_branch }}',
            'git push -u origin {{ cookiecutter.repo_main_branch }} v{{ cookiecutter.version }}'
        )
    )
{%- endif %}
    if not package_installed:
        commands.append('hatch env create default')

    commands.append('hatch shell')
{% if cookiecutter.pre_commit == 'yes' %}
    if not pre_commit_installed:
        commands.extend(('pre-commit install --install-hooks', 'pre-commit autoupdate'))
{% endif %}

    print('\n'.join(commands))
    cli_bin_name = '{{ cookiecutter.cli_bin_name }}'
    while cli_bin_name.endswith('.py'):
        cli_bin_name = cli_bin_name.removesuffix('.py')

        if cli_bin_name == '{{ cookiecutter.package_name }}':
            warn('''
┌───────────────────────────────────────────────────────────────────────┐
│ ERROR:                                                                │
│                                                                       │
│     Your result package is broken. Your bin script named              │
│     {0} │
│                                                                       │
│     Python automatically adds the location of scripts to              │
│     `sys.path`. Because of that, the bin script will fail             │
│     to import your package because it has the same name               │
│     (it will try to import itself as a module).                       │
│                                                                       │
│     To avoid this problem you have two options:                       │
│                                                                       │
│     * Remove the ".py" suffix from `cli_bin_name`. │
│                                                                       │
│     * Use a different `package_name` {1} │
└───────────────────────────────────────────────────────────────────────┘
'''.format(
                '"{{ cookiecutter.cli_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(cli_bin_name).ljust(32)))
            sys.exit(1)
        break
