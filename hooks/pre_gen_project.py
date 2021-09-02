import re
import sys
from collections import OrderedDict

yes = ['y','yes','Y','Yes'] 
no = ['n','no','N','No'] 
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Flutter module name. Please do not use a - and use _ instead' % module_name)
    sys.exit(1)
