import subprocess
import sys

location = input("local or remote shutdown? l/r:")
if location.lower == "r":
    pc = input("What is the PC name?:")
    hours = input("In how many hours would you like to shutdown?:")
    mins = input("In how many minutes would you like to shutdown?:")
    secs = (hours * 3600) + (mins * 60)
    subprocess.call(["shutdown", "-f", "-s", "/m \\\\", pc, "-t", str(secs)])
else:
    hours = input("In how many hours would you like to shutdown?:")
    mins = input("In how many minutes would you like to shutdown?:")
    secs = (hours * 3600) + (mins * 60)
    subprocess.call(["shutdown", "-f", "-s", "-t", str(secs)])
