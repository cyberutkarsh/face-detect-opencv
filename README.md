# face-detect-opencv
This a **multi-threaded queue** based implementation of Face detection using **OpenCV 2.4 and Python 2.7** This repo contains source code to detect human faces using the OpenCV HAAR classifiers. I have used multiple **HAAR** classfiers which will include custom trained classfiers(models) in the future so that we can reach close to 100% accuracy in detecting human faces in a picture. I will also be including a dockerfile soon to set up the environment and easy build and deployment.

> `Usage: python main.py`
>> Output: This will output number of faces detected in the images (it will loop over all images in the data folder) by each classifier and print it to the console

Also included is a utility file SaveVideoToImage.py, which can convert any video format to a series of images. 
> `Usage: python SaveVideoToImage.py <video file name>`
>> Output: This will save the corresponding images at the same location as the video file
