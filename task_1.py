import shutil
def task_1 (filename, rasp ='/home/stud/PythonProjects/unpack_1',
          copycat ='/home/stud/PythonProjects/unpack_2',
          mask = '*.html'):
    shutil.unpack_archive (filename,rasp)
    shutil.copytree (rasp,copycat,ignore =
                     shutil.ignore_patterns(mask))
files = 'masterclass.tar.gz'
task_1(files)