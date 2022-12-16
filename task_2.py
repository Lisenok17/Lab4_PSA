import os
def task_2(name):
	spisok = []
	files = [f for f in os.listdir(name) if os.path.isfile(os.path.join(name,f))]
	dirs = [f for f in os.listdir(name) if os.path.isdir(os.path.join(name,f))]
	return path, files,dirs

path = '/home/stud/PythonProjects/Directories'
print (task_2(path))