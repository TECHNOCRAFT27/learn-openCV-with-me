# 📸 How to Set Up Image, Video, and Webcam using OpenCV
import cv2 
import os
import numpy as np 

# 1️⃣ Read (Input) an Image 🖼️
image_path = "C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\opencv\\learn\\asset\\person.png"
img = cv2.imread(image_path)  # Load the image
print("read done")

# 2️⃣ Write (Output) an Image 💾
new_image_path = "C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\opencv\\learn\\asset\\new_person.png"
new_img = cv2.imwrite(new_image_path, img)  # Save the image to a new file
print("write done")

# 3️⃣ Show Image on Screen 🖥️
cv2.imshow('person', img)  # Display the image
cv2.waitKey(50)  # Wait for a short time
print("display done")

# 4️⃣ Play a Video 🎥
video_path = "C:\\Users\\DELL\\Documents\\Pramila khopade\\code project\\python\\opencv\\learn\\asset\\video.mp4"
video = cv2.VideoCapture(video_path)  # Load the video file
rate = True

while rate:
    rate, frame = video.read()  # Read video frame by frame

    if rate:
        cv2.imshow('video', frame)  # Show each frame
        cv2.waitKey(4)  # Adjust playback speed

video.release()  # Release the video resource
cv2.destroyAllWindows()  # Close all OpenCV windows

# 5️⃣ Webcam Streaming 🎦
rate = True

# Open webcam (0 = default camera)
webcam = cv2.VideoCapture(0)

# Show live webcam feed
while True:
    rate, frame = webcam.read()  # Read frames from webcam
 
    cv2.imshow('webcam', frame)  # Display webcam feed
    # Press 'q' to exit
    if cv2.waitKey(4) & 0xFF == ord('q'):
        break

webcam.release()  # Corrected typo (relese -> release)
cv2.destroyAllWindows()  # Close all windows
