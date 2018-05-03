import sys
from array import *
import re


if __name__=="__main__":
	
	# fileTime = {}
	# allType = ["src", "test", "others"]
	# for j in allType:
	# 	fileTime[(j, "0 sec")] = 0
	# 	fileTime[(j, "30 sec")] = 0
	# 	fileTime[(j, "1 min")] = 0
	# 	fileTime[(j, "5 min")] = 0
	# 	fileTime[(j, "10 min")] = 0
	# 	fileTime[(j, ">10 min")] = 0
	fileCount={"0sec":0, "30sec":0, "1min":0, "5min":0, "10min":0, ">10min":0}

	fileTime={"0sec":0, "30sec":0, "1min":0, "5min":0, "10min":0, ">10min":0}

	with open("fileTime.txt") as f:
		for line in f:
			item = ""
			#print (line)
			(key, val) = line.split("\t", 1)
			file = re.split("[ ]", key)
			#print(file)
			# for i in range(len(file)):
			#	print(file[i])
			#	print(len(file))
			# if "src" in file:
			# 	item = "src"
			# if "test" in file:
			# 	item = "test"
			# else: 
			# 	item = "others"
			
			time=int(val)
			
			if time==0:
				fileTime["0sec"] += len(file);
				fileCount["0sec"]+=1
			elif time>1 and time<=30:
				fileTime["30sec"] += len(file);
				fileCount["30sec"]+=1
			elif time> 30 and time<= 60:
				fileTime["1min"] += len(file);
				fileCount["1min"]+=1
			elif time > 60 and time<= 300:
				fileTime["5min"] += len(file);
				fileCount["5min"]+=1
			elif time > 300 and time <= 600:
				fileTime["10min"] += len(file);
				fileCount["10min"]+=1
			elif time > 600:
				fileTime[">10min"] += len(file);
				fileCount[">10min"]+=1

	with open(sys.argv[1], 'w') as file:
		for key, value in fileTime.items():
			if float(fileCount[key]) != 0:
				file.write(str(key)+ '\t' + str((float(value)/float(fileCount[key]))))
			else:
				file.write(str(key)+ '\t' + str("0"))
			file.write('\n')
		file.write('\n')