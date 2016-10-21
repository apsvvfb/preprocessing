import json
import sys
from pprint import pprint

ImgIDs=sys.argv[1]
inputfile="/home/c-nrong/VQA/question_answers.json"
with open(inputfile) as data_file:
	data=json.load(data_file)
#pprint(data)
'''
#id=1: data[0]
print data[0]["id"]
print data[0]["qas"][0]["question"]
print data[0]["qas"][1]["question"]
#id=2: data[1]
print data[1]["id"]
print data[1]["qas"][0]["question"]

#list: type(data)
#string: type(data[i]["id"]
#list: type(data[0]["qas"])
#dict: type(data[0]["qas"][0])
'''

newlist = sorted(data, key=lambda k: k['id'])
data=newlist 

f=open(ImgIDs,'r')
lines=f.readlines()
f.close()
for ix,line in enumerate(lines):
	outID=line.strip()
	print outID
	img=filter(lambda temp: temp['id'] == int(outID), data) #type of img is "list"
	if img[0]["id"] != int(outID):
		print "getQues.py: jsonID-"+str(img["id"])+" and imgID-"+outID+" are not same!" 
		sys.exit()
	outfile="Ques/q_"+outID+".txt"
	for que in img[0]["qas"]:
	   with open(outfile,'a') as f:	
		f.write(que["question"]+'\n')
		#print(outID+":"+que["question"])
		#sys.exit()	
