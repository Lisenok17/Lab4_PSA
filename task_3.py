import os
def task_3(path):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count('\\')
        indent = '\t' * level + ' ᒻ'
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = '\t' * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
task_3(path='/home/stud/PythonProjects/Directories')