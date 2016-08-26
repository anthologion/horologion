#!/usr/bin/python
import os, sys
import argparse
import time
from jinja2 import Environment, PrefixLoader, FileSystemLoader
SCRIPT_DIR=os.path.dirname(os.path.abspath(sys.argv[0]))
if __name__ is not "__main__":
    SCRIPT_DIR = __file__

def get_psalm(number):
    return u"Psalm " + unicode(number)

def generate_service(church, rite, language, trans, time):
    # For the time being, we wil just hardcode things. We can get fnacy later.
    common_elements = "%s/templates/%s/%s/%s/%s/common" % (SCRIPT_DIR, church, rite, language, trans)
    service_templates = "%s/templates/%s/%s/%s/%s" % (SCRIPT_DIR, church, rite, language, trans)
    global_macros = "%s/templates/" % (SCRIPT_DIR)
    loader = FileSystemLoader([common_elements,
                               service_templates,
                               global_macros])
    j_env = Environment(loader=loader)
    j_env.globals['psalm'] = get_psalm
    template = j_env.get_template('midnight.md')
    return template.render()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Given a Church, Rite, language, translation description, and time, generate HTML for a church service.')
    parser.add_argument('--church', const='c', type=str, nargs='?', default='oc')
    parser.add_argument('--rite', const='r', type=str, nargs='?', default='eastern')
    parser.add_argument('--language', const='l', type=str, nargs='?', default='en-us')
    parser.add_argument('--translation', const='t', type=str, nargs='?', default='hmbm')
    parser.add_argument('--datetime', const='d', type=str, nargs='?', default=time.strftime("%c"))

    args = parser.parse_args()
    print generate_service(args.church, args.rite, args.language,
                           args.translation, args.datetime)

