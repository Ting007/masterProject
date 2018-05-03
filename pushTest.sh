#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    cd ../PluginTest1
    git checkout $line
    git push origin $line:1.0release --force-with-lease
    echo "$line has been pushed to the github"
    sleep 15
    cd ../shellTest1
done < "$1"