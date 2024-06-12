from jinja2 import Environment
import pathlib

import pytest


@pytest.fixture(name='template_names')
def fixture_template_names(request):
    if request.node.get_closest_marker('repo_hosting').args[0] == 'github.com':
        return ('licenses.yml', 'publish.yml', 'tests.yml')
    elif request.node.get_closest_marker('repo_hosting').args[0] == 'gitlab.com':
        return ('licenses.yml', 'publish.yml', 'tests.yml')


class TestGithub:
    @staticmethod
    @pytest.mark.repo_hosting('github.com')
    @pytest.mark.template_dir('{{cookiecutter.repo_name}}/.github/workflows/')
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


class TestGitlab:
    @staticmethod
    @pytest.mark.repo_hosting('gitlab.com')
    @pytest.mark.template_dir('{{cookiecutter.repo_name}}/.gitlab/templates/')
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
