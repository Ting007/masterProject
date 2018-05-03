#!/bin/bash
git log --pretty="%h" > commits.txt #get all the ref of repo
./modified.sh commits.txt #relate ref from commits with the changed files
git log --pretty="%h %ci" > commitTime.txt #get all the time and ref of repo
python3 ./time_diff.py commitTime.txt mtime.txt #relates the ref with the time difference
python3 ./file_time.py fileTime.txt #relates the changed file with time difference
python3 ./typeModify.py typeTime.txt $1 #find the type of changed file with time difference
python3 ./fileModify.py fileCount.txt #count the average change file per commit at each time interval