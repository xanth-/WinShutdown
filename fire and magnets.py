import subprocess
import sys
yn = raw_input("shutdown computer s/r/c:")
if yn.lower() == 's':
    subprocess.call(["shutdown", "-f", "-s", "-t", "0"])
elif yn.lower() == 'r':
    subprocess.call(["shutdown", "-f", "-r", "-t", "0"])
else:
    print "ok"