#!/bin/bash
qsum=0
for qfile in `ls Ques/`
do
	qnum=`cat "Ques/$qfile" | wc -l`
	qsum=$[qsum+qnum]
done
echo $qsum

