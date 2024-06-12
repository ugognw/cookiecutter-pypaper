from jinja2 import Environment
import pathlib

import pytest


class TestPyProjectTOML:
    @staticmethod
    @pytest.mark.repo_hosting('github.com')
    @pytest.mark.template_dir('{{cookiecutter.repo_name}}')
    def test_render(cookie_config: dict, environment: Environment):
        filename = pathlib.Path('test_results/README.rst')
        template = environment.get_template('README.rst')
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(
                template.render(
                    cookiecutter=cookie_config
                )
            )