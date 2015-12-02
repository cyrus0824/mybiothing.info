import os
import re
import sys
from string import Template
import json
from shutil import copytree

def transform_name(s, d):
    return Template(re.sub(r"\}\}", "}", re.sub(r"\{\{", "${", s))).substitute(d)

def main(args):
    dir = os.path.abspath(args[1])

    template_dir = os.path.join(os.getcwd(), 'templates')
    
    if not os.path.exists(template_dir):
        print("Could not find template directory.  Exiting.")        
        sys.exit(1)

    copytree(os.path.abspath('biothings'), os.path.join(dir, 'biothings'))

    # Get settings dict
    f = open('project-settings.json', 'r')
    settings_dict = json.load(f)
    f.close()

    os.chdir(template_dir)

    # Template files out
    for (dirpath, dirnames, filenames) in os.walk(template_dir)[1:]:
        if os.path.isdir(dirpath):
            os.mkdir(os.path.join(dir, transform_name(os.path.relpath(dirpath), settings_dict)))
        elif os.path.isfile(dirpath):
            f = open(os.path.join(dir, transform_name(os.path.relpath(dirpath), settings_dict)), 'w')
            g = open(dirpath, 'r')            
            f.write(Template(g.read()).substitute(settings_dict))
            f.close()
            g.close()
            
    

if __name__ == '__main__':
    main(argv)