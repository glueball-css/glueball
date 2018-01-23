import os
import importlib

from ..settings import MODULES, MODULE_ROOT, CSS_ROOT, INCLUDES_DIR, INCLUDES


class StyleSheet:
    """Create a stylesheet

    Instance attributes
    -------------------
    name:       File is printed to <name>.css
    modules:    List of CSS Module objects to include
    module_dir: Directory to scan for modules
    """

    def __init__(self, name="glueball"):
        self.name = name
        self.modules = []
        self.module_dict = {}  # For convenience; to access modules from their slug
        self.load_modules()

    def add_module(self, mdl):
        self.modules.append(mdl)
        self.module_dict[mdl.get_slug()] = mdl

    def load_modules(self):
        """
        Load the CssModule instance from every module and add it.
        Look for a variable named "mdl".
        """
        fname = 'mdl'
        for dirslug in MODULES:
            try:
                self.add_module(importlib.import_module(MODULE_ROOT + '.' + dirslug + '.' + fname).mdl)
            except AttributeError:
                print("Skipped module %s: no 'mdl' variable found." % dirslug)
                continue

    def __getitem__(self, slug):
        """Get the module by its slug"""
        return self.module_dict[slug]

    def write_css(self):
        """Create a .css stylesheet file"""
        tpath = os.path.join(CSS_ROOT, self.name + '.css')

        # Create or clear the target file
        open(tpath, 'w').close()

        with open(tpath, "a") as tfile:
            # Append the various CSS includes
            for inclfile in INCLUDES:
                with open(os.path.join(INCLUDES_DIR, inclfile)) as ifile:
                    for line in ifile:
                        tfile.write(line)
            # Append the rules
            for line in str(self).splitlines():
                tfile.write(line + '\n')

    def __str__(self):
        version = "/*! GLUEBALL 0.0.1 | http://glueball.io */"
        header = """
/*
  ___  __    _  _  ____  ____   __   __    __   
 / __)(  )  / )( \(  __)(  _ \ / _\ (  )  (  )  
( (_ \/ (_/\) \/ ( ) _)  ) _ (/    \/ (_/\/ (_/\ 
 \___/\____/\____/(____)(____/\_/\_/\____/\____/
 
 
 */
 """
        includes = ''
        index = ''
        modules = "\n".join([str(mdl) for mdl in self.modules])
        return version + header + modules

if __name__ == "__main__":
    sheet = StyleSheet()
    sheet.write_css()
