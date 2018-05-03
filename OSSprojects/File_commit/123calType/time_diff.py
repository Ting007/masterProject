from datetime import datetime
import csv
import sys
from array import *
import re

def conv_date(date_str):
#	return datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y %z')
	return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S %z')
	
if __name__=="__main__":
	f = open(sys.argv[1], 'r')
	dis = f.readlines();
	f.close
	d1 = 0
	d2 = 0
	diff = 0
	commit = ""
	#diff_list = []
#	diff_count = {'0 sec':0, '30 sec':0, '60 sec':0, '5 min':0, '10 min':0, '> 10 min':0}
	file= open(sys.argv[2], 'w')
	for i in dis:
		#file = re.split("[. +]", key)
		filedate= re.split("[ ]", i, 1)
		# print(filedate)
		# print(filedate[0])
		# print(filedate[1])
		d2 = d1
		if filedate[1].endswith('\n'):
			d1=conv_date(filedate[1][:-1]);
		else:
			d1=conv_date(filedate[1]);

		if d2 != 0:
			diff = abs((d1-d2)).seconds
			file.write(str(diff) + "\n")
			commit = filedate[0]
			file.write(commit + "\t")
		else:
			commit = filedate[0]
			file.write(commit + "\t")
		    
	file.close
		