import datetime
import pytest

from jinja2 import Environment, FileSystemLoader


@pytest.fixture(name='repo_hosting')
def fixture_repo_hosting(request) -> str:
    if request.node.get_closest_marker('repo_hosting'):
        return request.node.get_closest_marker('repo_hosting').args[0]
    else:
        return 'gitlab.com'


@pytest.fixture(name='cookie_config')
def fixture_cookie_config(repo_hosting) -> dict:
    return {
        "full_name": "Ugochukwu Nwosu",
        "email": "ugognw@gmail.com",
        "website": "https://www.law-two.com",
        "project_name": "No Name",
        "project_short_description": "An example package. Generated with cookiecutter-pylibrary.",
        "package_name": "no_name",
        "distribution_name": "no-name",
        "repo_name": "python-no-name",
        "repo_hosting": repo_hosting,
        "repo_username": "ugognw",
        "repo_main_branch": "main",
        "release_date": "today",
        "year_from": str(datetime.datetime.now().year),
        "year_to": str(datetime.datetime.now().year),
        "keywords": "dog,gag",
        "version": "0.0.0",
        "license": "MIT license",
        "command_line_interface": "click",
        "cli_bin_name": "no-name",
        "support_type_checking": "yes",
        "pypi_badge": "yes",
        "pypi_disable_upload": "no",
        "coveralls": "yes",
        "codecov": "yes",
        "codacy" : "yes",
        "codacy_projectid" : "0000000",
        "codeclimate" : "yes",
        "gitchangelog": "yes",
        "github_actions": "yes",
        "gitlab_ci_cd": "yes",
        "pre_commit": "yes",
        "install_precommit_hooks": "yes",
        "pytest_datadir": "yes",
        "pytest_xdist": "yes",
        "sphinx_docs": "yes",
        "sphinx_theme": ["furo", "sphinx-rtd-theme", "python-docs-theme", "sphinx-py3doc-enhanced-theme", "sphinx-book-theme", "pydata-sphinx-theme"],
        "sphinx_doctest": "yes",
        "sphinx_docs_hosting": "https://no-name.readthedocs.io/",
        "initialize_git_repository": "yes",
        "install_package": "yes",
        "__repo_url": f"https://{repo_hosting}/ugognw/python-no-name",
    }


@pytest.fixture(name='template_dir')
def fixture_template_dir(request) -> str:
    marker = request.node.get_closest_marker('template_dir')
    if marker:
        return marker.args[0]
    else:
        return '.'


@pytest.fixture(name='environment')
def fixture_environment(template_dir) -> Environment:
    return Environment(
        loader=FileSystemLoader(
            template_dir
        ),
    )
    