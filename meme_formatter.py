from os import listdir 
from os.path import isfile, join
from PIL import Image, ImageDraw, ImageFilter
import random

bgdir = "resources/bgmemes"
memedir = "resources/memes"
newme = "resources/new_memes"

#get all background images
allbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]

#convert all background images to jpg for RGBA formatting in Pillow
for bg in allbg:
	if (bg.format != "JPEG"):
		#convert to jpg
		p_bg = bgdir+"/"+bg
		im = Image.open(p_bg)
		rgb_im = im.convert('RGB')
		newname = p_bg.partition('.')[0] + ".jpg"
		rgb_im.save(newname)

#get all memes
allmeme = [i for i in listdir(memedir) if isfile(join(memedir, i))]

for m in allmeme:
	#get path for random background meme
	ran = random.choice(allbg)
	
	#get paths & convert images to rgb
	bgpath = bgdir+"/"+ran
	mepath = memedir+"/"+m
	
	#open images
	bg = Image.open(bgpath)
	me = Image.open(mepath)
	i = True
	while(i):
		#make sure meme is smaller than bg
		if (bg.size < me.size):
			ran = random.choice(allbg)
			bgpath = bgdir+"/"+ran
			bg = Image.open(bgpath)
		elif(bg.size >= me.size):
			i = False
			#make backup copy
			back = bg.copy()
			
			#get middle of image
			pos = ((back.width - me.width)// 2,(back.height - me.height)//2)
			
			back.paste(me, pos)
			newname = newme+"/c_"+str(m)
			back.save(newname)
