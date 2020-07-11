import subprocess
import os
import re
base=os.getcwd()+"\\var\\123"
def _start(executable_file):
    return subprocess.Popen(
        "python -m pdb "+executable_file,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        # bufsize=1
    )
s=_start(base)
i=s.stdin
i.write(b"n\np asdfqweiubav123\n")
i.flush()
o=s.stdout
line=o.readline()
r=re.compile("asdfqweiubav123")
while r.search(line.decode()) is None:
    line=o.readline()