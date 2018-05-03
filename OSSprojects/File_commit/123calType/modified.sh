#!/bin/bash
cp /dev/null mfile.txt
commit1="0"
commit2="0"
while IFS='\n' read -r line || [[ -n "$line" ]]; do
	git config diff.renameLimit 999999
	commit2=${commit1}
    commit1=${line}
    #echo ${commit1}
    if [ ${commit2} != "0" ]
    then
        echo -e ${commit2}'\t'`git diff --name-only ${commit2} ${commit1}` >> mfile.txt
    fi
done < "$1"