{% if cookiecutter.command_line_interface == "click" -%}
from click.testing import CliRunner

{% endif -%}
{% if cookiecutter.command_line_interface != "no" -%}
from {{ cookiecutter.package_name }}.cli import main
{%- endif %}
{% if cookiecutter.command_line_interface == "no" -%}
from {{ cookiecutter.package_name }} import main
{%- endif %}

def test_main():
{%- if cookiecutter.command_line_interface == "click" %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == ""
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface == "argparse" %}
    main([])
{%- elif cookiecutter.command_line_interface == "plain" %}
    assert main([]) == 0
{%- else %}
    pass
{%- endif %}
