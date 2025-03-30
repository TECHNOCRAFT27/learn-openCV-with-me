import cv2
import os
import numpy as np

# blur image to reduce noice

# Image path
image_path = r"C:\Users\DELL\Documents\Pramila khopade\code project\python\learn openCV with me\asset\noise.png"

# Read image
img = cv2.imread(image_path)

# Blur intensity
intensity = 5  # Ensure it's odd for GaussianBlur

# Apply blur filters
blur_img = cv2.blur(img, (intensity, intensity))  # Simple blur
GaussianBlur_img = cv2.GaussianBlur(img, (intensity, intensity), 7)  # Gaussian blur
medianBlur_img=cv2.medianBlur(img,intensity)

# Show images
cv2.imshow('Original Image', img)
cv2.imshow('Blur Image', blur_img)
cv2.imshow('GaussianBlur Image', GaussianBlur_img)
cv2.imshow('medianBlur Image', medianBlur_img)

cv2.waitKey(0)
cv2.destroyAllWindows()




# Image path
img_path = "C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\learn openCV with me\\asset\\text.jpg"

# Read and resize image 📷
img = cv2.imread(img_path)
img = cv2.resize(img, (600, 600))

# Convert to grayscale 🖤💔
img_to_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Show grayscale image 👁️‍🗨️
cv2.imshow("text extract gray", img_to_gray)

# Simple Thresholding 📊
ret, thresh = cv2.threshold(img_to_gray, 140, 250, cv2.THRESH_BINARY)

# Adaptive Thresholding 🎨
ad_thresh = cv2.adaptiveThreshold(img_to_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 35, 20)

# Show thresholded images 👁️‍🗨️
cv2.imshow("text extract thresh", thresh)
cv2.imshow("text extract adaptive thresh", ad_thresh)

# Wait for key press ⏸️ and close windows ❌
cv2.waitKey(0)
cv2.destroyAllWindows()
