import sys
import numpy as np
import glob 
import h5py
import os
#imgpath=sys.argv[1]
numArea=5
pathTxt="AttenMaps/"
outpath="AttenMapsHdf5/"
ImgIDs="ImgIDs_ori.txt"
f=open(ImgIDs,'r')
lines=f.readlines()
f.close()
attenImg=np.ones((1,196))/196
for ix,line in enumerate(lines):
    outID=line.strip()
    print outID
    files=glob.glob("%s/%s_*.txt" %(pathTxt,outID))  
    #if len(files) >= numArea:
    attens=np.zeros((1,196*(len(files)+1)))
    attens[0:,0:196]=attenImg
    for fid,filename in enumerate(files):
	f=open(filename,'r')
	nums=f.read()
	f.close()
	atten=np.zeros(196)
	for i in range(0,196):
	    atten[i]=nums.split(' ')[i]
	atten=(atten-min(atten))/(max(atten)-min(atten))
	attens[0:,(fid+1)*196:(fid+2)*196]=atten
    if len(files) != 0:      
	outfile=os.path.join(outpath,outID+"_"+str(len(files))+".h5")
	with h5py.File(outfile, 'w') as hf:
            hf.create_dataset('areaprobs', data=attens)
    sys.exit()
