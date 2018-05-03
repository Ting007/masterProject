from datetime import datetime
import csv
import sys
from array import *

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
	#diff_list = []
	diff_count = {'0 sec':0, '30 sec':0, '60 sec':0, '5 min':0, '10 min':0, '> 10 min':0}
	for i in dis:
		d2 = d1
		if i.endswith('\n'):
			d1=conv_date(i[:-1])
		else:
			d1=conv_date(i)
		if d2 != 0:
			diff = abs((d1-d2)).seconds
		#	diff_list.append(diff)
			if diff==0:
				diff_count['0 sec'] = diff_count['0 sec'] + 1
			elif diff > 0 and diff <= 30:
				diff_count['30 sec'] = diff_count['30 sec'] +1
			elif diff > 30 and diff <= 60:
				diff_count['60 sec'] = diff_count['60 sec'] +1
			elif diff > 60 and diff <= 300:
				diff_count['5 min'] = diff_count['5 min'] + 1
			elif diff > 300 and diff <= 600:
				diff_count['10 min'] = diff_count['10 min'] + 1
			else:
				diff_count['> 10 min'] = diff_count['> 10 min'] + 1

	with open(sys.argv[2], 'a') as file:
		for key, value in diff_count.items():
			file.write(str(key+ '\t' + str(float(value)/float(sys.argv[3]))))
			file.write('\t')
		file.write('\n')