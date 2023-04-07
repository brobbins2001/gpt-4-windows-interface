import os
import json
import subprocess
import traceback
cwd = os.path.dirname(os.path.realpath(__file__))
os.chdir(cwd)
out = subprocess.Popen(['C:/WINDOWS/mingw32/bin/g++.exe', '--version'], cwd=cwd)
out.wait()
traceback.print_exc()
print(out.returncode)
print(out.stdout)
os.system('g++ -o program.exe program.cpp')
#out = subprocess.Popen(['g++', 'program.cpp', '-o program.exe'], cwd=cwd)