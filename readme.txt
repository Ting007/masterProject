-Plugin for regression test selection can be found in folder (Java 8):
automatedTestSelector
//It is under the maven tool and following the standard command of maven lifecycle.

-Script for module test selection can be found in folder:
moduleSelection/moduleSelection.sh
//It is a standard shell script to generare the module list for the changes code.
to run the script, run "./moduleSelection.sh" under the configuration/build/execute shell. or paste the code in window configuration/build/execute shell

-to simulte the commits from the commits ID or verion tag to the repo of projects:
first make sure the project has been clonded under ../PluginTest1 for jodatime or ../airliftTest

for testing of jodatime
./pushTest.sh branch2.txt or ./pushTest.sh branch3.txt

for testing of airlift
./pushTestAirlift.sh commits.txt

-The list of all the OSS on GITHUB can be found under folder OSSprojects.
fullList.csv  // random order of lists
fullListA-Z.csv // ordered by the program languages

-The URL and list of all the projects sorted by programming languages can be found in folder OSSprojects/URLlist
CplusProg.csv			
Cprog.csv		
JavaProg.csv		
phpProg.csv
JscriptProg.csv	
pyProg.csv
rbProg.csv
scalaProg.csv

-To automates the data analysis of GITHUB projects:

step 1: sparse the list of projects into URL of GITHUB
python ./sparseList.py  // take the name list of projects and turn into the GITHUB weblink.
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


step 2: 
--how to calculate the total number of commits in each repo? and the time interval of commits?
./calCommit.sh

-calCommit.sh
python ./sparseList.py ## generate the URL list (gitURL.csv) of the project list (projectList.csv).
./GitCommit.sh gitURL.csv ## take the URL list and calcuate the total number of commits in each repo history. GitCommit.sh will call time_diff.py. 
-to call time_diff.py calculate the time difference between commits
python time_diff.py <inputfile> <outputfile> <total_number_commits>

output:
comProj.csv # total number of commits in each projects and commit frequency
project_name.txt # log of commits in each projects

raw data: under the folder of OSSprojects/freqCommit
FreqResult.xlsx(overall data in sheet2)	comProj.csv	comProj1.csv	comProj3.csv	comProj4.csv

step 3:
--how to calculate the file composition per commits for projects? number of files per commits and the types of file
to calculate the changed file type of each repo, run the command under the folder of 123calType
./calTyep.sh fullList.csv

calType.sh will perform the command ./countModified.sh in File_commit/123calType

The code can be found under File_commit/123calType/

raw data can be found under folder File_commit:

CplusCount.csv		
RbCount.csv
PhpCount.csv
SlCount.csv
PyCount.csv
CprogCount.csv
JSCount.csv
JavaCount.csv

RbPect.csv
PhpPect.csv		
CplusPect.csv				
SlPect.csv
PyPect.csv		
CprogPect.csv
JavaPect.csv	
JSPect.csv		

rawDataCplus.xlsx		
RawDataJS.xlsx		
rawDataCprog.xlsx		
RawDataPhp.xlsx		
rawDataJava.xlsx
RawDataRb.xlsx		
rawdataPy.xlsx	
RawDataSl.xlsx
	


