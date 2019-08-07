import sys
from os import listdir
from os.path import isfile, join

if len(sys.argv) < 2:
    print("Need more arguments")
    exit(0)

ext = sys.argv[1]
legend = sys.argv[2]


only_files = [f for f in listdir(".") if isfile(join(".", f)) and (True if ext == "*" else f.endswith(ext))]

for file in only_files:
    print(file)
    f = open(file, "a+")
    lines = legend.split("\\n")
    for line in lines:
        f.write("\n")
        f.write(line)

