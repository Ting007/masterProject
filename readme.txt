Plugin for regression test selection can be found in folder (Java 8):
automatedTestSelector
//It is under the maven tool and following the standard command of maven lifecycle.

Script for module test selection can be found in folder:
moduleSelection/moduleSelection.sh
//It is a standard shell script to generare the module list for the changes code.
to run the script, run "./moduleSelection.sh" under the configuration/build/execute shell. or paste the code in window configuration/build/execute shell

to simulte the commits from the commits ID or verion tag to the repo of projects:
first make sure the project has been clonded under ../PluginTest1 for jodatime or ../airliftTest

for testing of jodatime
./pushTest.sh branch2.txt or ./pushTest.sh branch3.txt

for testing of airlift
./pushTestAirlift.sh commits.txt

The list of all the OSS on GITHUB can be found under folder OSSprojects.
fullList.csv  // random order of lists
fullListA-Z.csv // ordered by the program languages
CplusProg.csv			
Cprog.csv		
JavaProg.csv		
phpProg.csv
JscriptProg.csv	
pyProg.csv
rbProg.csv
scalaProg.csv

To automates the data analysis of GITHUB projects:

step 1: sparse the list of projects into URL of GITHUB
./sparseList.py  // take the name list of projects and turn into the GITHUB weblink.
In file sparseList.py, line 5 enter the file name of the input file, line 7 enter the name of the output file.
Generated project URL list:
gitURLSlProg.csv
gitURLCplusProg.csv
gitURLCprog.csv
gitURLJSProg.csv
gitURLJavaProg.csv
gitURLPhpProg.csv	
gitURLPyProg.csv
gitURLRbProg.csv

