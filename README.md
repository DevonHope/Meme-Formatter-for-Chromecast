# Meme-Formatter-for-Chromecast

# Description
  Formats memes for a google chromecast so they can be displayed as the wallpaper on a TV
  
  DISCALIMER:
  This is a work in progress, works with most memes but some memes that are larger than your background memes 
  might not appear to be centered correctly
  
  
# USE
 
  PREREQS
  1. Your computer must run python3 or higher
  2. You must install pip, use: python3 -m install pip
  3. You must install PIL (depreciated) or Pillow, use: pip install Pillow or easy_install Pillow
  4. Add your own meme backgrounds to the bgmemes folder inside resources: resources/bgmemes
  5. Add your own memes to resources/memes
  
  NOTE: all memes must be smaller in pixel size than the background memes. This will be focused upon and 
  fixed later but for now is only functioning in this manner for now.
  
  RUN
  1. Run the convert_image.py file to convert any background images from other formats to JPG
  2. Use: python3 meme_formatter.py
  
  NOTE: convert_image will be integrated into meme_formatter once the deletion problem is fixed.
        Images converted are not deleted automatically
