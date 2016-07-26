import exifread
from PIL import Image
from PIL.ExifTags import TAGS

print"""
 _____        _   __    ____              _      _
| ____|__  __(_) / _|  / ___| _ __  __ _ | |__  | |__    ___  _ __
|  _|  \ \/ /| || |_  | |  _ | '__|/ _` || '_ \ | '_ \  / _ \| '__|
| |___  >  < | ||  _| | |_| || |  | (_| || |_) || |_) ||  __/| |
|_____|/_/\_\|_||_|    \____||_|   \__,_||_.__/ |_.__/  \___||_|

# Extract exif data from picture with two methods
# Coded By karim Shoair | D4Vinci
# All Copyright To Squnity Company Team & Deveolopers
"""
photo=raw_input("\nPhoto Name : ")
print "\n[1] Method one\n"
img =Image.open(photo)
exif = img._getexif()
for tag in exif:
    tagname= TAGS.get(tag,tag)
    value=exif[tag]
    print str(tagname) +" : "+str(value)
print "-"*10

print "\n[2] Method Two\n"
f = open(photo, 'rb')
tags = exifread.process_file(f)
for tag in tags:
    value=tags[tag]
    if tag not in ['JPEGThumbnail']:
        print str(tag) +" : "+str(value)
