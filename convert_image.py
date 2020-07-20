from PIL import Image, ImageDraw, ImageFilter
from os import listdir 
from os.path import isfile, join
from pathlib import Path

bgdir = "resources/bgmemes"

#get all background images
allbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]

for bg in allbg:
	p_bg = bgdir+"/"+bg
	im = Image.open(p_bg)
	print(bg)
	print(im.format)

	if (im.format != 'JPEG'):
		print("\n")
		print("not jpg")
		print(bg)
	"""
		#convert to jpg
		rgb_im = im.convert('RGB')
		newname = p_bg.partition('.')[0] + ".jpg"
		rgb_im.save(newname)
		print("\n")
		print(bgdir+"/"+bg)
		#rmfile = Path(str(bgdir+"/"+bg))
		#rmfile.unlink()
	else:
		print("\n")
		print("jpg")
		print(bg)
	"""