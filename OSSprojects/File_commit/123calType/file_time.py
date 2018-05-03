import csv
import sys
from array import *

if __name__=="__main__":
	refFile={}
	refTime={}
	with open("mfile.txt") as f:
		for line in f:
			(key, val) = line.split("\t", 1)
			refFile[key] = val
			
	with open("mtime.txt") as h:
		for line in h:
			(key, val) = line.split("\t")
			refTime[key] = val
			
	output = open(sys.argv[1], 'w')
	for key1 in refFile.keys():
		for key2 in refTime.keys():
			if key1 == key2:
				output.write(refFile[key1][:-1] + '\t' + refTime[key2])
