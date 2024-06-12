from jinja2 import Environment
import pathlib

import pytest


class TestPostGenHook:
    @staticmethod
    @pytest.mark.repo_hosting('github.com')
    @pytest.mark.template_dir('hooks')
    def test_render(cookie_config: dict, environment: Environment):
        filename = pathlib.Path('test_results/post_gen_project.py')
        template = environment.get_template('post_gen_project.py')
        with open(filename, mode='w', encoding='utf-8') as file:
            file.write(
                template.render(
                    cookiecutter=cookie_config
                )
            )