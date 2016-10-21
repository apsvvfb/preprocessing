import sys
import numpy as np
import glob 
import h5py
import os
#imgpath=sys.argv[1]

numArea=5
pathTxt="AttenMaps/"
outfile="AttenMapsHdf5/train.hdf5"
#ImgIDs="ImgIDs_ori.txt"
ImgIDs="trainIDs.txt"

f=open(ImgIDs,'r')
lines=f.readlines()
f.close()
attenprobs=np.zeros((len(lines),numArea))
aid=-1
attenImg=np.ones((1,196))/196
for ix,line in enumerate(lines):
  outID=line.strip()
  print outID
  files=glob.glob("%s/%s_*.txt" %(pathTxt,outID))  
  if len(files) >= numArea:
     aid=aid+1
     attens=np.zeros((1,196*(numArea+1)))
     attens[0:,0:196]=attenImg
     for fid,filename in enumerate(files):
	if fid < numArea:
	   f=open(filename,'r')
	   nums=f.read()
	   f.close()
	   atten=np.zeros(196)
	   for i in range(0,196):
	       atten[i]=nums.split(' ')[i]
	   atten=(atten-min(atten))/(max(atten)-min(atten))
	   attens[0:,(fid+1)*196:(fid+2)*196]=atten
     attenprobs[aid]=attens
with h5py.File(outfile, 'w') as hf:
  hf.create_dataset('areaprobs', data=attenprobs)
#sys.exit()
