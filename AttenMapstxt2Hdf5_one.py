import sys
import numpy as np
import glob 
import h5py
import os
#imgpath=sys.argv[1]

pathTxt="AttenMaps/"
outfile="AttenMapsHdf5/AreaAll.hdf5"
IDfiles=["trainIDs.txt","testIDs.txt"]
for tid, ImgIDs in enumerate(IDfiles):
  f=open(ImgIDs,'r')
  lines=f.readlines()
  f.close()
  attenImgs  = np.ones((len(lines),196))/196
  attenprobs = np.zeros((len(lines),196))

  for ix,line in enumerate(lines):
     outID=line.strip()
     print outID
     files=glob.glob("%s/%s_*.txt" %(pathTxt,outID))  
     attens=np.zeros((len(files),196))
     for fid,filename in enumerate(files):
	   f=open(filename,'r')
	   nums=f.read()
	   f.close()
	   atten=np.zeros(196)
	   for i in range(0,196):
	       atten[i]=nums.split(' ')[i]
	   atten=(atten-min(atten))/(max(atten)-min(atten))
	   attens[fid]=atten
     attenprobs[ix]=np.sum(attens, axis=0)/len(files)
  final=np.hstack((attenImgs,attenprobs))
  if tid == 0:
	trainmatrix=final 
  else:
	testmatrix=final

with h5py.File(outfile, 'w') as hf:
   hf.create_dataset('trainareaprobs', data=trainmatrix)
   hf.create_dataset('testareaprobs', data=testmatrix)
