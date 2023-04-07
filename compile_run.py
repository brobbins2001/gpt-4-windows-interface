import os
import json
import subprocess

def system_call(command):
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()

def execute(response):
    output = json.loads(response['message']['content'])

    cpp_code = output['code']


    # Save C++ code to file
    with open('program.cpp', 'w') as file:
        file.write(cpp_code)

    # Compile C++ code
    os.system('g++ program.cpp -o program.exe')

    # Run executable
    os.system('program.exe')


    input("press enter to finish")
    # Delete files
    os.remove('program.cpp')
    os.remove('program.exe')