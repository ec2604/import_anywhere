import os
import sys
from inspect import currentframe
try:
    if os.name == 'nt':
        dir_names = os.environ['IMPORT_ANYWHERE_DIRS'].split(';')
    else:
        dir_names = os.environ['IMPORT_ANYWHERE_DIRS'].split(':')
except KeyError:
    print("Please set the environment variable IMPORT_ANYWHERE_DIRS", sys.stderr)
    sys.exit(1)
#Get frame for checking who imported
frame = currentframe().f_back
#Skip over irrelevant frames
while frame.f_code.co_filename.startswith('<frozen'):
    frame = frame.f_back
#current frame is file that imported package
importer_filename = os.path.realpath(frame.f_code.co_filename)
#Check where parent directory is located
for dir_name in dir_names:
    try:
        stop_idx = importer_filename.split(os.sep).index(dir_name)
        ancestor_path = os.sep.join(importer_filename.split(os.sep)[:stop_idx+1])
        #Append to sys path
        sys.path.append(ancestor_path)
    except ValueError:
        continue

