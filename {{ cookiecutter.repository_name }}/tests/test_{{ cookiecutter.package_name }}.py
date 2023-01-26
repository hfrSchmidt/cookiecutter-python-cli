#!/usr/bin/env python

"""Tests for `{{ cookiecutter.package_name }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
{%- endif %}

from {{ cookiecutter.package_name }} import {{ cookiecutter.package_name }}
{%- if cookiecutter.command_line_interface|lower == 'click' %}
from {{ cookiecutter.package_name }} import cli
{%- endif %}

{%- if cookiecutter.use_pytest == 'y' %}
{%- if cookiecutter.command_line_interface|lower == 'click' %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.package_name }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
{%- endif %}
{%- endif %}
