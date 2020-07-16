#!/usr/bin/python3
import os
import sys

files = []


def get_files(path):
    file_list = os.listdir(path)
    for tmp in file_list:
        tmp_path = os.path.join(path, tmp)
        if os.path.isfile(tmp_path):
            files.append(tmp_path)
        elif os.path.isdir(tmp_path):
            get_files(tmp_path)


for i in range(1, len(sys.argv)):
    if os.path.isfile(sys.argv[i]):
        files.append(sys.argv[i])
    elif os.path.isdir(sys.argv[i]):
        get_files(sys.argv[i])

output = ""
for file in files:
    output += " \"" + file + "\""

os.system("gtkhash" + output)
