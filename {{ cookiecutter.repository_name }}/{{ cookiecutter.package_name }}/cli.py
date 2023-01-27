"""Console script for {{ cookiecutter.package_name }}."""

{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click
{%- endif %}
import sys

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{ cookiecutter.package_name }}."""
    click.echo("Place your code into "
               "{{ cookiecutter.package_name }}.cli.main")
    return 0
{%- endif %}

if __name__ == "__main__":
    sys.exit(main())