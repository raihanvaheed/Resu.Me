import sys
import os

if not sys.argv:
    print("need to specify file path")
    sys.exit(1)

file_name = sys.argv[1]
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

f = open("{}/{}".format(ROOT_DIR, file_name), "r")
for line in f:
    print(line)