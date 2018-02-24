# import_anywhere
This package allows relative imports no matter where the script is run from.

This is to avoid situations where packages are used and relative imports only work when the script
is run from its actual location. This package requires the user to list all "parent directories" which
 the package is to  look for in the "IMPORT_ANYWHERE_DIRS" environment variable.

An example of this problem
If a script is located within a package with the following tree for example:

 - MY_PARENT_FOLDER  
 ----- PACKAGE_A  
 --------  C  
 ------------- USEFUL_SCRIPT.PY  
 --------- MY_SCRIPT.PY

And MY_SCRIPT contains the line "import C.USEFUL_SCRIPT.PY", this won't work if I'm running MY_SCRIPT.PY
from a different directory.

import_anywhere solves this problem if C (or PACKAGE_A) are located in the IMPORT_ANYWHERE_DIRS environment variable.

