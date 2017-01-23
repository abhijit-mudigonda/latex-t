#!/bin/bash

clear 

set -e
#Stop on an error inside a pipeline
set -o pipefail
#Throw an error on calling an unassigned variable
set -u

#DEFAULTS
directory='./ICFHR_package/CROHME2011_data/CROHME_training'

#NONDEFAULTS

#inkml files consist of multiple traces, which are sets of coordinates for that particular stroke. We want to parse just the trace parts, to get a list of coordinates, and then draw all the strokes on a blank image to create a training image. 

for file in $(ls $directory | grep TrainData | shuf)
do
	echo "Processing $file"
	#Make a 50x50 pixel image file
	echo "Making a file"
	#Remove all newlines (make it one line)
	tr -d '\n' < $directory/$file > temp0.txt
	#add a new line at the trace close tags
	sed 's/<trace/\n<trace/g' temp0.txt > temp1.txt
	sed 's/trace>/trace>\n/g' temp1.txt > temp2.txt
	#remove lines without trace id
	grep "trace id" temp2.txt > temp3.txt
	#make it just CSVs
	sed 's/>/>\n/g' temp3.txt > temp4.txt
	sed 's/</\n</g' temp4.txt > temp5.txt
	sed '/trace/d' temp5.txt > temp6.txt
	sed '/^$/d' temp6.txt > temp7.txt
	sed 's/,//g' temp7.txt > finalcoordinates.txt

	rm temp*

	cat finalcoordinates.txt | python strokedrawer.py --destination ./ --name out
	display out.png
done
