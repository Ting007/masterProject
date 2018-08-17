##This project presents a broad evaluation of the testing process of CI for the projects on the GITHUB.<\BR> 
We use large historical data of GITHUB projects to figure out the important metrics of the open source project to improve the efficiency, convenience, time saving and labor saving of the software project testing. 
This paper provides several bar chart view for the adapted test algorithm which could be used in open source project with CI and aims to be a stepping stone for academia to provides more efficient time frame for the software testing.

##BarChart
![BarChart 1](/testing.pdf)
![BarChart 2](/commits_distribution.pdf)
![BarChart 3](/numbers.pdf)
![BarChart 4](/composition.pdf)

Files:
folder OSSprojets includes all the metrics analysis of projects
folder automatedTestSelector is a plugin for the jenkins regression test selection
folder moduleSelection is a script for the module test selection.
file branch2.txt and branch3.txt is a sequence of commits for joda-time for repo PluginTest1.
file commits.txt is a sequency of commits for aiflift module test selection.
pushTest.sh is used to simulate the changes of code to joda-time (repo PluginTest1)
pushTestAirlift.sh is used to simulate the changes of code to airliftTest.


-Plugin for regression test selection can be found in folder (Java 8):
automatedTestSelector
##It is under the maven tool and following the standard command of maven lifecycle.

-Script for module test selection can be found in folder:
moduleSelection/moduleSelection.sh
##It is a standard shell script to generare the module list for the changes code.
to run the script, run "./moduleSelection.sh" under the configuration/build/execute shell. or paste the code in window configuration/build/execute shell

-to simulte the commits from the commits ID or verion tag to the repo of projects:
first make sure the project has been clonded under ../PluginTest1 for jodatime or ../airliftTest

for testing of jodatime
./pushTest.sh branch2.txt or ./pushTest.sh branch3.txt

for testing of airlift
./pushTestAirlift.sh commits.txt

-The list of all the OSS on GITHUB can be found under folder OSSprojects.
OSSprojects/fullList.csv  ##random order of lists
OSSprojects/ullListA-Z.csv ##ordered by the program languages

-The URL and list of all the projects sorted by programming languages can be found in folder OSSprojects/URLlist
CplusProg.csv			
Cprog.csv		
JavaProg.csv		
phpProg.csv
JscriptProg.csv	
pyProg.csv
rbProg.csv
scalaProg.csv

Generated project URL list under the same fold URLlist:
gitURLSlProg.csv
gitURLCplusProg.csv
gitURLCprog.csv
gitURLJSProg.csv
gitURLJavaProg.csv
gitURLPhpProg.csv	
gitURLPyProg.csv
gitURLRbProg.csv


raw data for commit frequency: under the folder of OSSprojects/freqCommit
FreqResult.xlsx(overall data in sheet2)	
comProj.csv	
comProj1.csv	
comProj3.csv	
comProj4.csv



File_commit/123calType/

raw data of file compositin and file counter per commit can be found under folder File_commit:

File count:
CplusCount.csv		
RbCount.csv
PhpCount.csv
SlCount.csv
PyCount.csv
CprogCount.csv
JSCount.csv
JavaCount.csv

File type percentate:
RbPect.csv
PhpPect.csv		
CplusPect.csv				
SlPect.csv
PyPect.csv		
CprogPect.csv
JavaPect.csv	
JSPect.csv		

raw data summary in excel and normalized
rawDataCplus.xlsx		
RawDataJS.xlsx		
rawDataCprog.xlsx		
RawDataPhp.xlsx		
rawDataJava.xlsx
RawDataRb.xlsx		
rawdataPy.xlsx	
RawDataSl.xlsx
	


