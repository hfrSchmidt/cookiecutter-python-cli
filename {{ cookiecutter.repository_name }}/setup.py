#!/usr/bin/env python

import io
import os

import setuptools

dependencies = ["python-freeipa >= 1.0"]


# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

history_filename = os.path.join(package_root, "HISTORY.rst")
with io.open(history_filename, encoding="utf-8") as history_file:
    history = history_file.read()

# Only include packages under the 'infra' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package for package in setuptools.find_packages() if package.startswith("infra")
]

# Determine which namespaces are needed.
namespaces = ["infra"]
if "infra.usermgmt" in packages:
    namespaces.append("infra.usermgmt")


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
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: POSIX :: Linux",
        "Topic :: System :: Systems Administration",
    ],
    packages=packages,
    namespace_packages=namespaces,
    install_requires=dependencies,
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
)
