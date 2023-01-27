import re
import sys


PACKAGE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

package_name = '{{ cookiecutter.package_name }}'

if not re.match(PACKAGE_REGEX, package_name):
    print('ERROR: %s is not a valid Python module name!' % package_name)

    # exits with status 1 to indicate failure
    sys.exit(1)