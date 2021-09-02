#!/usr/bin/env python
import os
import re
import shutil

module_name = '{{ cookiecutter.project_slug}}'
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(*filepath):
    print("remove file " + os.path.join(PROJECT_DIRECTORY, *filepath))
    os.remove(os.path.join(PROJECT_DIRECTORY, *filepath))

if __name__ == '__main__':

    # License
    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        remove_file('LICENSE')

    print("The project (%s) initialized, keep up the good work!" % module_name)