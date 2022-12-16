import os
import pathlib

def task_4(path, mask):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count('\\')
        indent = '\t' * level + 'ᒻ '
        print('{}{}/'.format(indent, pathlib.PurePath(root).name))
        subindent = '\t' * (level + 1)
        for f in files:
            if mask in f:
                print('{}{}'.format(subindent, f))
task_4(path='/home/stud/PythonProjects/Directories', mask='.png')