import datetime
import pytest

from jinja2 import Environment, FileSystemLoader


@pytest.fixture(name='cookie_config')
def fixture_cookie_config() -> dict:
    return {
        "full_name": "Ugochukwu Nwosu",
        "email": "ugognw@gmail.com",
        "website": "https://www.law-two.com",
        "package_name": "no_name",
        "distribution_name": "no-name",
        "repo_name": "python-no-name",
        "project_name": "No Name",
        "project_short_description": "An example package. Generated with cookiecutter-pylibrary.",
        "repo_username": "ugognw",
        "repo_main_branch": "main",
        "year_from": str(datetime.datetime.now().year),
        "year_to": str(datetime.datetime.now().year),
        "keywords": "dog,gag",
        "chemistry_related": "yes",
        "physics_related": "yes",
        "license": "MIT license",
        "version": "0.0.0",
        "command_line_interface": "click",
        "cli_bin_name": "no-name",
        "support_type_checking": "yes",
        "pypi_disable_upload": "no",
        "pre_commit": "yes",
        "install_precommit_hooks": "yes",
        "pytest_datadir": "yes",
        "pytest_xdist": "yes",
        "initialize_git_repository": "yes",
        "install_package": "yes",
        "__date": str(datetime.datetime.now().year),
        "__repo_url": "https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}",
        "_extensions": [
            "pylibrary.JsonQuoteExtension",
            "jinja2_time.TimeExtension"
        ]
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
    