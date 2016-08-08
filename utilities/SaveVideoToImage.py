import cv2
import sys

file_path = sys.argv[1]
video_object = cv2.VideoCapture(file_path)

i=0
success = True
while success:
    success,frame = video_object.read()
    if success:
        cv2.imwrite(file_path[:-4]+"_"+str(i)+".jpg",frame)
	i+=1
print("Done!")
