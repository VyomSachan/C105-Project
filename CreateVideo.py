import cv2
import os

path = "C105ProjImages/"
images = []

for file in os.listdir(path):
    name, extension = os.path.splitext(file)
    if extension in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        file_name = path + "/" + file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter("Project.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)

for i in range(count):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")