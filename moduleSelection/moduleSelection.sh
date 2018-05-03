#!/bin/bash

check_rc() {
  # exit if passed in value is not = 0
  # $1 = return code
  # $2 = command / label
  if [ $1 -ne 0 ]
  then
    echo "$2 command failed"
    exit 1
  fi
}
echo 'git fetch'
check_rc $? 'echo git fetch'
git fetch
check_rc $? 'git fetch'
echo 'git diff --name-only origin/testbase'
lastID=`git log --format="%H" -n 2`


check_rc $? 'echo git diff'
diff_files=`git diff --name-only ${lastID}| xargs`
#diff_files=`git diff --name-only 6d3d6c968d97415320cf44b646dea4de382af9ba c3acef7ba7cef62e28945782c91f1da956e67306 | xargs`
check_rc $? 'git diff'

modList=()
for x in ${diff_files}
do
  #echo "${x}"
  if [[ ${x} = *"java"* ]]
  then 
    check_rc $? "java character detected in ${x},"
    module=`echo ${x} | cut -d '/' -f 1`
    if [[ "${modList[@]}" =~ "${module}" ]]
    then
      echo "yep, it's there"
    else
  	  modList+=("${module}")
    fi
  fi
done

for x in ${modList[@]}
do
  echo ${x}
  mvn test -pl ${x} -fn
done