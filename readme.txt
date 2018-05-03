to simulte the commits from the commits ID or verion tag to the repo of projects:

first make sure the project has been clonded under ../PluginTest1 for jodatime or ../airliftTest

for testing of jodatime
./pushTest.sh branch2.txt or ./pushTest.sh branch3.txt

for testing of airlift
./pushTestAirlift.sh commits.txt

Plugin for regression test selection can be found in folder:
automatedTestSelector
//It is under the maven tool and following the standard command of maven lifecycle.