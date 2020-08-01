import os
from os import listdir
from os.path import isfile, join
from PIL import Image, ImageFile

def formatMemes(sub):
	ImageFile.LOAD_TRUNCATED_IMAGES = True
	bgdir = "resources/bgmemes"
	memedir = "resources/sub_"+sub
	fixme = "resources/fixed_"+sub

	#get all background images
	allbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]

	#convert all background images to jpg for RGBA formatting in Pillow
	for bg in allbg:
		ext = bg.split('.')[1]
		if (ext != "jpg"):
			#convert to jpg
			p_bg = bgdir+"/"+bg
			im = Image.open(p_bg)
			rgb_im = im.convert('RGB')

			#remove old file
			os.remove(p_bg)

			newname = p_bg.partition('.')[0] + ".jpg"
			rgb_im.save(newname)

	#get all memes
	allmeme = [i for i in listdir(memedir) if isfile(join(memedir, i))]
	newbg = [im for im in listdir(bgdir) if isfile(join(bgdir, im))]
	print()
	printPB(0, len(allmeme), prefix='Fixing:',suffix='Done',length=50)
	for i, m in enumerate(allmeme):
		m_ext = m.split('.')[1]
		if(m_ext != 'gif' or m_ext != 'gifv'):
			#get path for random background meme
			ran = random.choice(newbg)

			#get paths & convert images to rgb
			bgpath = bgdir+"/"+ran
			mepath = memedir+"/"+m

			#open images
			bg = Image.open(bgpath)
			me = Image.open(mepath)

			o = True
			while(o):
				#find ratios
				rat_w = (me.width / bg.width) * 100
				rat_h = (me.height / bg.height) * 100

				#if the ratio is below %50 find smaller background
				if(rat_h <= 75 and rat_w <= 75):
					r_val = 1.25
					me = me.resize((round(me.size[0]*r_val), round(me.size[1]*r_val)))

				elif(me.width > bg.width or me.height > bg.height):
					#resize memes that are too big for any background
					#resizes them to %80
					r_value = .80
					#print('resized ' +m)
					if(rat_h >= 100 and rat_w >= 100):
						me = me.resize((round(me.size[0]*r_value), round(me.size[1]*r_value)))
					elif(rat_w >= 100):
						me = me.resize((round(me.size[0]*r_value), round(me.size[1]*1)))
					elif(rat_h >= 100):
						me = me.resize((round(me.size[0]*1), round(me.size[1]*r_value)))
				#make sure meme is smaller than bg
				elif (bg.width < me.width and bg.height < me.height):
					ran = random.choice(newbg)
					bgpath = bgdir+"/"+ran
					bg = Image.open(bgpath)

				elif(bg.width >= me.width and bg.height >= me.height):
					printPB(i+1, len(allmeme), prefix='Fixing:',suffix='Done',length=50)
					#print('Fixing image '+m)
					o = False
					#make backup copy
					back = bg.copy()

					#get middle of image
					pos = ((back.width - me.width)// 2,(back.height - me.height)//2)

					back.paste(me, pos)
					newname = fixme+"/c_"+str(m)
					back.save(newname)
					
	def main():
		sub = 'resources/memes'
		formatMemes(sub)

	if __name__ == "__main__":
		try:
			main()
		except KeyboardInterrupt:
			print()
			print('UGH! I almost dropped my croissant!')
			try:
				sys.exit(0)
			except SystemExit:
				os._exit(0)
