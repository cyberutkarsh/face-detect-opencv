import numpy as np
import cv2
import sys

#Define the classifiers
frontalface_default_classifier = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')
frontalface_alt_classifier = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt.xml')
frontalface_alt2_classifier = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt2.xml')
frontalface_alt_tree_classifier = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt_tree.xml')
profileface_classifier = cv2.CascadeClassifier('classifiers/haarcascade_profileface.xml')

#Front face classification
def classify_frontface(imagepath):
	detected = 0
	#get the input image and convert to grayscale
        img = cv2.imread(imagepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = frontalface_default_classifier.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                detected += 1
       	print 'FrontalFace Classfier detected-' + str(detected)

def classify_frontface_alternate1(imagepath):
	detected = 0
	#get the input image and convert to grayscale
        img = cv2.imread(imagepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = frontalface_alt_classifier.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                detected += 1
        print 'FrontalFace Alt. 1 Classfier detected-' + str(detected)

def classify_frontface_alternate2(imagepath):
        detected = 0
	#get the input image and convert to grayscale
        img = cv2.imread(imagepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = frontalface_alt2_classifier.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                detected += 1
        print 'FrontalFace Alt. 2 Classfier detected-' + str(detected)

def classify_frontalface_alt_tree(imagepath):
	detected = 0
	#get the input image and convert to grayscale
        img = cv2.imread(imagepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = frontalface_alt_tree_classifier.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,128,128),2)
                roi_gray = gray[y:y+h, x:x+w]
                detected += 1
        print 'FrontalFace Alt. Tree Classfier detected-' + str(detected)

def classify_profileface(imagepath):
	detected = 0
	#get the input image and convert to grayscale
        img = cv2.imread(imagepath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = profileface_classifier.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
                roi_gray = gray[y:y+h, x:x+w]
                detected += 1
        print 'ProfileFace Classfier detected-' + str(detected)