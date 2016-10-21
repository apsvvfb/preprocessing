import sys
import numpy as np
from scipy import misc
from PIL import Image
import os 

imgpath=sys.argv[1]
filename=sys.argv[2]
outpath=sys.argv[3]
question=sys.argv[4]
#1.generate Attention Map
f=open(filename,'r')
nums=f.read()
f.close()
atten=np.zeros(196)
img=np.ones((448,448))
for i in range(0,196):
	atten[i]=nums.split(' ')[i]
atten=(atten-min(atten))/(max(atten)-min(atten))
atten=np.floor(atten*255)
#atten=atten.reshape(14,14)
#print max(atten),min(atten)
for i in range(0,14):
	r=i*32
	for j in range(0,14):
	   c=j*32
	   mul=atten[i*14+j]
	   for ri in range(r,r+31):
		for cj in range(c,c+31):
		    img[ri][cj]=img[ri][cj]*mul
misc.toimage(img, cmin=0.0, cmax=255.0).save('atten.png')
#sys.exit()
#2.reshape the original image
img = Image.open(imgpath) # image extension *.png,*.jpg
new_width  = 448
new_height = 448
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('test448.jpg')
#3.overlay two images
background = Image.open("test448.jpg")
overlay = Image.open("atten.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.7)
outfile="%s/%s_%s.png" % (outpath,os.path.basename(filename).split('.')[0],question.split('?')[0])
new_img.save(outfile,"PNG")

os.remove("test448.jpg")
os.remove("atten.png")
