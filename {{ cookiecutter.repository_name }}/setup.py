#!/usr/bin/env python

import io
import os

import setuptools

dependencies = [{%- if cookiecutter.command_line_interface | lower == 'click'%}'Click>=8.0',{%- endif%}]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

history_filename = os.path.join(package_root, "HISTORY.rst")
with io.open(history_filename, encoding="utf-8") as history_file:
    history = history_file.read()

# Only include packages under the '{{ cookiecutter.package_name }}' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package for package in setuptools.find_packages() if package.startswith("{{ cookiecutter.package_name }}")
]

# Determine which namespaces are needed, when namespaced packages are supposed to be used
# namespaces = ["{{ cookiecutter.package_name }}"]
# if "{{ cookiecutter.package_name }}.<namespace>" in packages:
#     namespaces.append("{{ cookiecutter.packe_name }}.<namespace>")

setuptools.setup(
    name="{{ cookiecutter.repository_name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    license="{{ cookiecutter.open_source_license }}",
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repository_name }}",
    classifiers=[
        "{{ cookiecutter.release_status }}",
{%- if cookiecutter.open_source_license in license_classifiers %}
        "{{ license_classifiers[cookiecutter.open_source_license] }}",
{%- endif %}
{%- for audience_item in coookiecutter.classifiers.audience %}
        "{{ audience_item }}",
{%- endfor %}
{%- for os_item in coookiecutter.classifiers.os %}
        "{{ os_item }}",
{%- endfor %}
{%- for topic_item in coookiecutter.classifiers.topic %}
        "{{ topic_item }}",
{%- endfor %}
        "Programming Language :: Python",
{%- for py_version_item in coookiecutter.classifiers.python_versions %}
        "Programming Language :: Python :: {{ py_version_item }}",
{%- endfor %}
    ],
    packages=packages,
    # namespace_packages=namespaces,
    install_requires=dependencies,
{%- if 'n' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.package_name }}={{ cookiecutter.package_name }}.cli:main',
        ],
    },
{%- endif %}
    python_requires=">={{ cookiecutter.min_python_version }}",
    include_package_data=True,
    zip_safe=False,
)
