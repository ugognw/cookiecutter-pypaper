from jinja2 import Environment
import pathlib

import pytest


class TestGithub:
    @staticmethod
    def test_render(cookie_config: dict, environment: Environment, template_names: list[str], template_dir: str):
        for template_name in template_names:
            filename = pathlib.Path(f'test_results/{template_dir}') / template_name
            template = environment.get_template(template_name)
            with open(filename, mode='w', encoding='utf-8') as file:
                file.write(
                    template.render(
                        cookiecutter=cookie_config
                    )
                )
