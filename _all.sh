#!/bin/bash
mPATH=`pwd`
imgPath=$mPATH/Images/
imgIDs=$mPATH/ImgIDs.txt
####################.download img and get the imgIDs
####--input : url 
####--output: images(saved in $imgPath) + $imgIDs(sorted)
#./getImg.sh $imgPath $imgIDs

####################.generate question
####----input: $imgIDs
####----output: questions for all images("Ques/q_${imgID}.txt")
#python genQues.py $imgIDs


cd /home/c-nrong/VQA/HieCoAttenVQA/

while read imgID 
do
   quesFile=$mPATH/Ques/q_${imgID}.txt
   ii=0
   while read Question 
   do
      ii=$[ii+1]
      if [ $ii -le 8 ];then
	echo "imgID:$imgID, QuesID:$ii"
	#echo `date`
	#################.generate attention map 
	#####/home/c-nrong/VQA/HieCoAttenVQA/genAttenMap.lua: copied from predict.lua
	#####I changed the /home/c-nrong/VQA/HieCoAttenVQA/misc/question_level.lua
	#####----input: one image + one question
	#####----output: one txt(question.txt)
	#cd /home/c-nrong/VQA/HieCoAttenVQA/
	Question=${Question/\?/ \?}
	th genAttenMap.lua "${imgPath}/${imgID}.jpg" "$Question"
	tail -n 1 question.txt > "$mPATH/AttenMaps/${imgID}_AttenMap_${ii}.txt"
	rm question.txt

	#if [ $ii -eq 8 ];then	echo `date` && exit -1; 	fi

	#################.draw attenmap+oriImg
	#####----input: question.txt + one image
	#####----output: one image
	#cd $mPATH
	#python draw.py "${imgPath}/${imgID}.jpg" "./AttenMaps/${imgID}_AttenMap_${ii}.txt" "$mPATH/OutImg/" "$Question"
      fi
   done < $quesFile
done < $imgIDs
