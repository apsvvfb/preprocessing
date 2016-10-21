#!/bin/bash
imgPath=$1
imgIDs=$2
web=http://imdev-demo.dscv.miniy.yahoo.co.jp:15820/20160727/vgj/p
for((pageID=1;pageID<=280;pageID++))
do
	if [ -r "index.html" ];then
		rm index.html
	fi
	url="${web}/${pageID}/"
	wget $url
	if [ -r "imgUrls.txt" ];then
		rm imgUrls.txt
	fi
	python getImgUrl.py imgUrls.txt
	while read imgUrl
	do
		echo $imgUrl
		wget -P $imgPath $imgUrl
		#exit -1
	done < imgUrls.txt	
done

ls -1 $imgPath | cut -d'.' -f1 > imgtemp
sort -n imgtemp > $imgIDs
rm imgtemp 


