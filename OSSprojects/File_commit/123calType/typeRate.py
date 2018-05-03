import sys
from array import *
import re

def file_type(commits):
	allType=[]
	with open("typeTime.txt") as f:
		fileType = []
		for line in f:
			# (key, val) = line.split("\t", 1)
			type = re.split("[	\t+]", line)
			print("key is " + type[0])
			print("val is " + type[1])
			print("last is " + type[-1])
			fileType.append(type[0])
		allType=list(set(fileType))
	print(allType)		
	return allType


if __name__=="__main__": 
	if (int(sys.argv[2]) > 0):
	 	allType=file_type(int(sys.argv[2]))