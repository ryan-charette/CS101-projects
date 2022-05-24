<<comment
In this project, you’ll use the commands you learned to navigate and edit the filesystem of this special shop.
The starting filesystem is shown below.
bicycle-world-ii
|—— brands.txt
|—— freight/
|   |—— messenger/
|   |—— porteur/
|—— mountain/
|   |—— downhill/
|   |   |—— heavyweight/
|   |   |—— lightweight/
|   |—— hardtail/
|—— racing/
    |—— road/
    |—— track/
comment
#Print the working directory.
pwd
#List the files and directories in the working directory.
ls
#Change directories to the freight/ directory
cd freight
#List the files and directories in the working directory.
ls
#Change directories to the porteur/ directory
cd porteur
#Change directories up two levels to the bicycle-world-ii/ directory.
cd ../..
#List the files and directories in the bicycle-world-ii/ directory.
ls
#Change directories to the mountain/downhill/ directory.
cd mountain/downhill
#Make a file called dirt.txt
touch dirt.txt
#Make a file called mud.txt
touch mud.txt
#List the files and directories in the downhill/ directory.
ls
#Downhill biking is dangerous: In the downhill/ directory, make a directory called safety/.
mkdir safety
#Change directories to the bicycle-world-ii/ directory.
cd ../..
#List the contents of the bicycle-world-ii/ directory.
ls
#The shop is adding a new type of bike! In bicycle-world-ii/, make a directory called bmx/.
mkdir bmx
#Without changing directories from bicycle-world-ii/, make a file in the bmx/ directory called tricks.txt.
touch bmx/tricks.txt
#List the files and directories in the current directory.
ls
