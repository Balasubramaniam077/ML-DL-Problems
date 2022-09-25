# from PIL import Image
# import os, sys

# img_dir = "E:/DATASET/plant-docx-village/corn/corn/train/Cercospora_leaf_spotGray_leaf_spot/"
# dirs = os.listdir( img_dir )

# def resize_bulk_images():
# 	for img in dirs:
# 		if os.path.isfile(img_dir + img):
# 			im = Image.open(img_dir + img)
# 			f, e = os.path.splitext(img_dir + img)
# 			imResize = im.resize((224, 224), Image.ANTIALIAS)
# 			imResize.save(f + '_resized.jpg', 'JPEG', quality=90)

# print('Bulk images resizing started...')
# resize_bulk_images()
# print('Bulk images resizing finished...')



import PIL
import os
import os.path
from PIL import Image

f = r'E:/DATASET/plant-doc/plantdocx-corn/PlantDoc-Dataset/corn/test/Corn Gray leaf spot'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((224,224))
    img.save(f_img)
print("image are Resized")