#!/usr/bin/env python3
import os
from PIL import Image 

image_path=[]
root_path = 'images'

#get all the file names in the root path and save them in a list
for root,dirs,files in os.walk(root_path):
  for file in files:
    image_path.append(file)
    
#rotate, resize, convert the file type to .jpeg and save in designated path
def transform(path):
  if not path.endswith('.DS_Store'):
    im = Image.open(f"{root_path}/{path}")
    im.rotate(90).resize((128,128)).convert("RGB").save(f"opt/icons/{path}", "JPEG")

for images in image_path:
  transform(images)

