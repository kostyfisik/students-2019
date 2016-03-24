#!/usr/bin/python
fname = "names"
with open(fname) as f:
    array = []
    for line in f:
        name = line.split()
        name_dot = name[0][0]+'.'+name[1]
        array.append(name_dot.lower())
print(array)

import subprocess
res = subprocess.check_output(["git", "branch"])
branches=[]
for line in res.splitlines():
    branches.append(line.strip())
print(branches)

for name in array:
    if not name in branches:
        res = subprocess.check_output(["git", "branch",name])
    res = subprocess.check_output(["git", "checkout",name])
    for line in res.splitlines():
        print(line)
    res = subprocess.check_output(["git", "push", "--set-upstream", "origin", name])
    for line in res.splitlines():
        print(line)
    print("git branch "+name)
# process the output line by line
