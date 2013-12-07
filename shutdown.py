import subprocess
import sys

hours = input("In how many hours would you like to shutdown:")
mins = input("In how many minutes would you like to shutdown:")
secs = (hours * 3600) + (mins * 60)
subprocess.call(["shutdown", "-f", "-s", "-t", str(secs)])
