from PIL import Image, ImageDraw, ImageFilter
from os import listdir 
from os.path import isfile, join

bgdir = "bgmemes"

#get all background images
allbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]

for bg in allbg:
	if (bg.format != "JPEG"):
		#convert to jpg
		p_bg = "bgmemes/"+bg
		im = Image.open(p_bg)
		rgb_im = im.convert('RGB')
		newname = p_bg.partition('.')[0] + ".jpg"
		rgb_im.save(newname)