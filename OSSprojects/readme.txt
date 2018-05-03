under the folder of OSSprojects:
-To automates the data analysis of GITHUB projects:

Part 1: under the folder shellTest1/OSSprojects/URLlist
sparse the list of projects into URL of GITHUB
In file sparseList.py, line 5 enter the file name of the input file, line 7 enter the name of the output file.
under the folder shellTest1/OSSprojects/freqCommit, execute the command:
python ./sparseList.py  ## take the name list of projects and turn into the GITHUB weblink.

Generated project URL list under the path shellTest1/OSSprojects/URLlist:
gitURLSlProg.csv
gitURLCplusProg.csv
gitURLCprog.csv
gitURLJSProg.csv
gitURLJavaProg.csv
gitURLPhpProg.csv	
gitURLPyProg.csv
gitURLRbProg.csv


Part 2: under the folder shellTest1/OSSprojects/freqCommit 
--how to calculate the total number of commits in each repo? and the time interval of commits?
execute the command:
./calCommit.sh

-calCommit.sh
1) python ./sparseList.py ## generate the URL list (gitURL.csv) of the project list (projectList.csv).
2)./GitCommit.sh gitURL.csv ## take the URL list from URLlist and calcuate the total number of commits in each repo history. GitCommit.sh will call time_diff.py. 
3)python time_diff.py <inputfile> <outputfile> <total_number_commits> ##to call time_diff.py calculate the time difference between commits

output of calCommit.sh:
comProj.csv # total number of commits in each projects and commit frequency
project_name.txt # log of commits in each projects

raw results data for commits per commits: under the folder of OSSprojects/freqCommit
FreqResult.xlsx(overall data in sheet2)	
comProj.csv	
comProj1.csv	
comProj3.csv	
comProj4.csv

Part 3: under the folder OSSprojects/File_commit
--how to calculate the file composition per commits for projects? number of files per commits and the types of file
to calculate the changed file type of each repo, run the command under the folder of 123calType
./calTyep.sh fullList.csv

calType.sh will perform the command ./countModified.sh in File_commit/123calType

The code can be found under File_commit/123calType/

raw data can be found under folder File_commit:

number of files per commits:
CplusCount.csv		
RbCount.csv
PhpCount.csv
SlCount.csv
PyCount.csv
CprogCount.csv
JSCount.csv
JavaCount.csv

Percentage of file types per commits:
RbPect.csv
PhpPect.csv		
CplusPect.csv				
SlPect.csv
PyPect.csv		
CprogPect.csv
JavaPect.csv	
JSPect.csv		

Normalized data of percentage of file type per commits:
rawDataCplus.xlsx		
RawDataJS.xlsx		
rawDataCprog.xlsx		
RawDataPhp.xlsx		
rawDataJava.xlsx
RawDataRb.xlsx		
rawdataPy.xlsx	
RawDataSl.xlsx