# the_imported.py
import os
import sys
from inspect import currentframe
top_directory_name = 'package_name'
#Get frame for checking who imported
frame = currentframe().f_back
#Skip over irrelevant frames
while frame.f_code.co_filename.startswith('<frozen'):
    frame = frame.f_back
#current frame is file that imported package
importer_filename = os.path.realpath(frame.f_code.co_filename)
#Check where parent directory is located
stop_idx = importer_filename.split(os.sep).index(top_directory_name)
ancestor_path = os.sep.join(importer_filename.split(os.sep)[:stop_idx+1])
#Append to sys path
sys.path.append(ancestor_path)
