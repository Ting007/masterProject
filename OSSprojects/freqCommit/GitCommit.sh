#!/bin/bash
cp /dev/null comProj4.csv #the output file needs to be cleaned 
while IFS='\n' read -r line || [[ -n "$line" ]]; do
    http=${line}
    fileArray=$(echo $line | cut -d '/' -f 5 | cut -d '.' -f 1)
   	git clone ${http} ${fileArray} 
    cd /Users/ting/Documents/${fileArray}
    git log --pretty=format:%ci > ${fileArray}.txt #fileArray.txt is the log file of git versions control
    echo `wc -l ${fileArray}.txt` >> /Users/ting/Documents/comProj4.csv #the results of the file is comProj4.csv please change it according ly
    commits=$(wc -l ${fileArray}.txt)
    #python time_diff.py inputfile outputfile total_number_commits
    python3 /Users/ting/Documents/123openSourcePJ/time_diff.py ${fileArray}.txt /Users/ting/Documents/comProj4.csv ${commits}
    cd /Users/ting/Documents
done < "$1"

# this shell will read the input from the command line 
#
