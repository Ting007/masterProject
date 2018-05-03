import csv
from array import *

if __name__=="__main__":
	with open('scalaProg.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile) #read the program list from the file
		with open('gitURLSlProg.csv', 'w') as file:
			for row in reader:
				#print("http://github.com/"+row['owner_login']+"/"+row['repo_name']+".git")
				file.write("http://github.com/"+row['owner_login']+"/"+row['repo_name']+".git/")
				file.write('\n')