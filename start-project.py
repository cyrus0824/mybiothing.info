import os
import re
import sys
from string import Template
import json
from shutil import copytree
from shutil import rmtree

def transform_name(s, d):
    return Template(re.sub(r"\}\}", "}", re.sub(r"\{\{", "${", s))).substitute(d)

def usage():
    return "Usage: python start-project.py < path-to-project-directory >"

def main(args):
    try:    
        dir = os.path.abspath(args[1])
    except IndexError:
        print("Valid project destination directory must be included.")
        print(usage())
        sys.exit(1)        
      
    template_dir = os.path.join(os.getcwd(), 'biothings', 'templates')
    
    if not os.path.exists(template_dir):
        print("Could not find template directory.  Exiting.")        
        sys.exit(1)

    copytree(os.path.abspath('biothings'), os.path.join(dir, 'biothings'))
    rmtree(os.path.join(dir, 'biothings', 'templates'))   

    # Get settings dict
    f = open('project-settings.json', 'r')
    settings_dict = json.load(f)
    f.close()

    os.chdir(template_dir)

    # Template files out
    for (dirpath, dirnames, filenames) in list(os.walk(template_dir))[1:]:
        #print(dirpath)
        #print(filenames)
        thisdir = os.path.join(dir, transform_name(os.path.relpath(dirpath), settings_dict))
        os.mkdir(thisdir)
        for fi in filenames:
            f = open(os.path.join(thisdir, transform_name(fi, settings_dict)), 'w')
            g = open(os.path.join(os.path.abspath(dirpath), fi), 'r')            
            f.write(Template(g.read()).substitute(settings_dict))
            f.close()
            g.close()

if __name__ == '__main__':
    main(sys.argv)