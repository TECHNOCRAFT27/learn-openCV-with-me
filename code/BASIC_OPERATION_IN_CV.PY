# 🔥 BASIC_OPERATION_IN_CV
#📭 all import
import cv2 
import os
import numpy as np

#🐱‍💻 property to change size

#1️⃣ resize image

# 📷 image path
image_path="C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\learn openCV with me\\asset\\person.png"

# cv2 image step up

img = cv2.imread(image_path)
print("original size: ",img.shape)

# resized image dimension
resize_img=cv2.resize(img,(600,300))
print("resized image size: ",resize_img.shape)

# saving resize image to location
resize_img_path="C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\learn openCV with me\\asset\\resize_person.png"


resize_image= cv2.imwrite(resize_img_path,resize_img)# (location,img we want to save name)
print("check asset folder")


# 2️⃣ croping image
# 📷 image path
image_path="C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\learn openCV with me\\asset\\person.png"

# cv2 image step up

img = cv2.imread(image_path)

# crop_image

# Define correct cropping indices (y1:y2, x1:x2)
crop_img = img[800:1200, 400:1000]  # Switched start and stop

cv2.imshow('crop image',crop_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

# 3️⃣ colour filter image
# 📷 image path
image_path="C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\learn openCV with me\\asset\\person.png"

# cv2 image step up
img = cv2.imread(image_path)

# format colur
BGRtoRGB =cv2.COLOR_BGR2RGB
BGRtoGray= cv2.COLOR_BGR2GRAY

img_rgb=cv2.cvtColor(img,BGRtoRGB)


cv2.imshow('rgb img',img_rgb)
cv2.waitKey(0)

cv2.destroyAllWindows()
