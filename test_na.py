import json 
import sys
import numpy as np
filename="question_answers.json"
#filename="/home/c-nrong/VQA/draw/Json/question_answers_jan.json"
train = json.load(open(filename, 'r'))
#print(len(train))
ids=np.zeros(len(train))
allq=0
for i in range(len(train)):
    #imgID=train[i]["image"]
    #ids[i]=imgID
    numq=len(train[i]["qas"])
    allq=allq+numq
print(allq)
sys.exit()
#finids=np.unique(ids)
#np.savetxt('test.out', finids, delimiter=',',fmt='%d')
unique, counts = np.unique(ids, return_counts=True)
print dict(zip(unique, counts))
#print(np.unique(counts))




