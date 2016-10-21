require 'image'

imname="demo_img1.jpg"
im=image.load(imname,3,'float') 
im=image.scale(im,448, 448) 
image.save("test448.jpg", im)
