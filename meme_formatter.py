from os import listdir 
from os.path import isfile, join
from PIL import Image, ImageDraw, ImageFilter
import random

bgdir = "bgmemes"
memedir = "memes"

#get all background images
allbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]

#get all memes
allmeme = [i for i in listdir(memedir) if isfile(join(memedir, i))]

for m in allmeme:
	#get path for random background meme
	ran = random.choice(allbg)
	
	#get paths & convert images to rgb
	bgpath = "bgmemes/"+ran
	mepath = "memes/"+m
	
	#open images
	bg = Image.open(bgpath)
	me = Image.open(mepath)
	i = True
	while(i):
		#make sure meme is smaller than bg
		if (bg.size < me.size):
			ran = random.choice(allbg)
			bgpath = "bgmemes/"+ran
			bg = Image.open(bgpath)
		elif(bg.size >= me.size):
			i = False
			#make backup copy
			back = bg.copy()
			
			#get middle of image
			pos = ((back.width - me.width)// 2,(back.height - me.height)//2)
			
			back.paste(me, pos)
			newname = "new_memes/c_"+str(m)
			back.save(newname)