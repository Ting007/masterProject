#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    cd ../airliftTest
    git checkout $line
    git push origin $line:testbase --force-with-lease
    echo "$line has been pushed to the github"
    sleep 30
    cd ../shellTest1
done < "$1"