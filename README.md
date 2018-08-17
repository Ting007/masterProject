## This project presents a broad evaluation of the testing process of CI for the projects on the GITHUB.<br /> 


We use large historical data of GITHUB projects to figure out the important metrics of the open source project to improve the efficiency, convenience, time saving and labor saving of the software project testing.<br />


This paper provides several bar chart view for the adapted test algorithm which could be used in open source project with CI and aims to be a stepping stone for academia to provides more efficient time frame for the software testing.<br />
<!-- ![Dependence Analysis for Regression Testing Selection](/OSSprojects/graphs/dependency.pdf) -->
### Dependence Analysis for Regression Testing Selection
<object data="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/dependency.pdf" type="application/pdf" width="200px" height="200px">
    <embed src="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/dependency.pdf">
        <p>This browser does not support PDFs. Please follow the link to view it: <a href="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/dependency.pdf">view PDF</a>.</p>
    </embed>
</object>

## BarChart
### Time Interval Vs Commits
<object data="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/commits_distribution.pdf" type="application/pdf" width="200px" height="200px">
    <embed src="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/commits_distribution.pdf">
        <p>This browser does not support PDFs. Please follow the link to view it: <a href="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/commits_distribution.pdf">view PDF</a>.</p>
    </embed>
</object>

### Files at Different Time Interval
<object data="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/numbers.pdf" type="application/pdf" width="400px" height="700px">
    <embed src="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/numbers.pdf">
        <p>This browser does not support PDFs. Please follow the link to view it: <a href="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/numbers.pdf">view PDF</a>.</p>
    </embed>
</object>


### File Types at Different Time interval
<object data="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/composition.pdf" type="application/pdf" width="400px" height="700px">
    <embed src="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/composition.pdf">
        <p>This browser does not support PDFs. Please follow the link to view it: <a href="https://github.com/Ting007/masterProject/blob/master/OSSprojects/graphs/composition.pdf">view PDF</a>.</p>
    </embed>
</object>

## Files:
folder OSSprojets includes all the metrics analysis of projects
folder automatedTestSelector is a plugin for the jenkins regression test selection
folder moduleSelection is a script for the module test selection.
file branch2.txt and branch3.txt is a sequence of commits for joda-time for repo PluginTest1.
file commits.txt is a sequency of commits for aiflift module test selection.
pushTest.sh is used to simulate the changes of code to joda-time (repo PluginTest1)
pushTestAirlift.sh is used to simulate the changes of code to airliftTest.


-Plugin for regression test selection can be found in folder (Java 8):
automatedTestSelector
#### It is under the maven tool and following the standard command of maven lifecycle.

-Script for module test selection can be found in folder:
moduleSelection/moduleSelection.sh
#### It is a standard shell script to generare the module list for the changes code.
to run the script, run "./moduleSelection.sh" under the configuration/build/execute shell. or paste the code in window configuration/build/execute shell

-to simulte the commits from the commits ID or verion tag to the repo of projects:
first make sure the project has been clonded under ../PluginTest1 for jodatime or ../airliftTest

for testing of jodatime
./pushTest.sh branch2.txt or ./pushTest.sh branch3.txt

for testing of airlift
./pushTestAirlift.sh commits.txt

-The list of all the OSS on GITHUB can be found under folder OSSprojects.
#### random order of lists
OSSprojects/fullList.csv
#### ordered by the program languages  
OSSprojects/ullListA-Z.csv 

-The URL and list of all the projects sorted by programming languages can be found in folder OSSprojects/URLlist
CplusProg.csv <br />			
Cprog.csv <br />
JavaProg.csv <br />		
phpProg.csv <br />
JscriptProg.csv	<br />
pyProg.csv <br />
rbProg.csv <br />
scalaProg.csv <br />

Generated project URL list under the same fold URLlist:
gitURLSlProg.csv <br />
gitURLCplusProg.csv <br />
gitURLCprog.csv <br />
gitURLJSProg.csv <br />
gitURLJavaProg.csv <br />
gitURLPhpProg.csv <br />	
gitURLPyProg.csv <br />
gitURLRbProg.csv <br />


raw data for commit frequency: under the folder of OSSprojects/freqCommit
FreqResult.xlsx(overall data in sheet2)	
comProj.csv	 <br />
comProj1.csv <br />
comProj3.csv <br />
comProj4.csv <br />



File_commit/123calType/

raw data of file compositin and file counter per commit can be found under folder File_commit:

File count:
CplusCount.csv<br />
RbCount.csv<br />
PhpCount.csv<br />
SlCount.csv<br />
PyCount.csv<br />
CprogCount.csv<br />
JSCount.csv<br />
JavaCount.csv<br />

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
	


