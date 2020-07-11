import subprocess
import os
import re

class subpdb: # pdb subprocess 관리
    def __init__(self,filepath):
        self.filepath=filepath
        self.sub=self._start(self.filepath)
    def __del__(self):
        # self.thr.do_run=False
        self.sub.kill()
        # print("stop")
    def query(self,message):
        self.inp(message)
        return self.outp()
    def inp(self,message):
        i=self.sub.stdin
        i.write((message+"\np asdfqweiubav123\n").encode())
        i.flush()
    def outp(self):
        o=self.sub.stdout
        line=o.readline().decode()
        lines=[line]
        r=re.compile("asdfqweiubav123")
        while r.search(line) is None:
            line=o.readline().decode()
            lines.append(line)
        return lines
    def _start(self,executable_file):
        return subprocess.Popen(
            "python -m pdb "+executable_file,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            # bufsize=1
        )
