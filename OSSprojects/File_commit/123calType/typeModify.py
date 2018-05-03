import sys
from array import *
import re

# def file_type():
# 	allType=[]
# 	with open("fileTime.txt") as f:
# 		fileType = []
# 		for line in f:
# 			(key, val) = line.split("\t", 1)
# 			file = re.split("[. +]", key)
			
# 			for i in range(len(file)):
# 				if len(file[i]) < 5:
# 					fileType.append(file[i])
# 		allType=list(set(fileType))
# 		allType.append("test")
# 	#	print(allType)		
# 	return allType


if __name__=="__main__":
	
	fileTime = {}
	allType = ["src", "test", "others"]
	for j in allType:
		fileTime[(j, "0 sec")] = 0
		fileTime[(j, "30 sec")] = 0
		fileTime[(j, "1 min")] = 0
		fileTime[(j, "5 min")] = 0
		fileTime[(j, "10 min")] = 0
		fileTime[(j, ">10 min")] = 0

	with open("fileTime.txt") as f:
		for line in f:
			item = ""
			(key, val) = line.split("\t", 1)
			file = re.split("[/. +]", key)
			#print(file)
			# for i in range(len(file)):
			# 	print(file[i])
			
			if "test" in file:
				item = "test"
			elif "src" in file:
				item = "src"
			elif "source" in file:
				item = "src"
			elif ("rb" or "js" or "css" or "cpp" or "c" or "py" or "java" or "sh" or "php" or "scala") in file:
				item = "src"
			else: 
				item = "others"
			
			time=int(val)
			
			if time==0:
				fileTime[(item, "0 sec")] += 1;
			elif time>1 and time<=30:
				fileTime[(item, "30 sec")] += 1;
			elif time> 30 and time<= 60:
				fileTime[(item, "1 min")] += 1;
			elif time > 60 and time<= 300:
				fileTime[(item, "5 min")] += 1;
			elif time > 300 and time <= 600:
				fileTime[(item, "10 min")] += 1;
			elif time > 600:
				fileTime[(item, ">10 min")] += 1;

	with open(sys.argv[1], 'w') as file:
		for key, value in fileTime.items():
			if int(sys.argv[2]) != 0:
				file.write("	".join(key)+ '\t' + str((float(value)/float(sys.argv[2]))))
				file.write('\n')
			else:
				file.write("	".join(key)+ '\t' + "0")
				file.write('\n')
		file.write('\n')
 