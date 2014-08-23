import sys
import os
import re

def getRoVersion(v):
	if v[0]<4:
		return "0"
	elif v[0]<5:
		return "1024"
	elif not(v[0]>=7 and v[1]>=2):
		return "2049"
	elif v[0]<8:
		return "3074"
	else:
		return "4096"

def getSpiderVersion(v):
	if v[3]<7:
		return "1024"
	elif v[3]<11:
		return "2050"
	elif v[3]<16:
		return "3074"
	else:
		return "4096"

def getCnVersion(v):
	if v[4]=="J":
		return "JPN"
	else:
		return "WEST"

def getFirmVersion(v):
	if v[0]<5:
		return "OLD_MEMMAP"
	else:
		return "NEW_MEMMAP"


#format : "X.X.X-XR"
version=sys.argv[1]
p=re.compile("^([0-9]+)\.([0-9]+)\.([0-9]+)-([0-9]+)([EUJ])")
r=p.match(version)

if r:
	cverMajor=int(r.group(1))
	cverMinor=int(r.group(2))
	cverMicro=int(r.group(3))
	nupVersion=int(r.group(4))
	nupRegion=r.group(5)
	v=(cverMajor, cverMinor, cverMicro, nupVersion, nupRegion)
	os.system("make clean")	
	os.system("make CNVERSION="+getCnVersion(v)+" ROVERSION="+getRoVersion(v)+" SPIDERVERSION="+getSpiderVersion(v)+" FIRMVERSION="+getFirmVersion(v))
else:
	print("invalid version format; learn2read.")
