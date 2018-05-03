#!/bin/bash
while IFS='\n' read -r line || [[ -n "$line" ]]; do
    http=${line}
    fileArray=$(echo $line | cut -d '/' -f 5 | cut -d '.' -f 1)
   	#git clone ${http} ${fileArray}
    echo ${fileArray}
    if [ -d "/Users/ting/Documents/${fileArray}" ]; then
         cp -r /Users/ting/Documents/123calType /Users/ting/Documents/${fileArray}/
    fi

    if [ -d "/Users/ting/Documents/${fileArray}/123calType" ]; then
        cd /Users/ting/Documents/${fileArray}/123calType
        commits=$(wc -l commits.txt)
        ./countModified.sh ${commits}
    fi
    cd /Users/ting/Documents
done < "$1"