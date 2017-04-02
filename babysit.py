#!/usr/bin/env python3
import sys
import subprocess

cmd = sys.argv[1:]


cont = True
while cont:
  p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
  try:
    p.wait()
  except KeyboardInterrupt:
    cont = False
