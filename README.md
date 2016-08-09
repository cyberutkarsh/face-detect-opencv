# face-detect-opencv
This a **multi-threaded queue** based implementation of Face detection using **OpenCV 2.4 and Python 2.7** This repo contains source code to detect human faces using the OpenCV HAAR classifiers. I have used multiple **HAAR** classfiers which will include custom trained classfiers(models) in the future so that we can reach close to 100% accuracy in detecting human faces in a picture. I have also added a Dockerfile for dockerized environment setup. 

## Code Usage

> `Usage: python main.py`
>> Output: This will output number of faces detected in the images (it will loop over all images in the data folder) by each classifier and print it to the console

Also included is a utility file SaveVideoToImage.py, which can convert any video format to a series of images. 
> `Usage: python SaveVideoToImage.py <video file name>`
>> Output: This will save the corresponding images at the same location as the video file

## Docker Setup Instructions
These instructions basically help you install docker and setup the environment based on the included Docker file

### Docker Install
* Follow this link - [https://docs.docker.com/engine/installation/mac/] to install docker natively on mac, there are also other links if you want to install on Windows or other linux based OSes
* After install docker, be sure to run the hello-docker to test your installation, and if you see a "network time out issue" , here [http://stackoverflow.com/questions/31990757/network-timed-out-while-trying-to-connect-to-https-index-docker-io] is a good resource to troubleshoot that.

### Setup environment based using Dockerfile
> 
* Clone the repo using `git clone git@github.com:cyberutkarsh/face-detect-opencv.git`
* Change directory to the repo directory `cd face-detect-opencv`
* Build the docker image using the docker build command `docker build --no-cache -t face-detect-ubuntu-opencv-python:1.0 .`
* After the build completes run `docker images` to make sure that the image was successfully created. You should see a image with REPOSITORY NAME face-detect-ubuntu-opencv-python abdandand TAG as 1.0
* Start a docker container with the docker run command with interative shell and the image we just build `docker run -i -t face-detect-ubuntu-opencv-python:1.0 /bin/bash`
* Change to your home directory `cd` Create your work directory e.g. projects `mkdir projects` and then clone the repo using `git clone git@github.com:cyberutkarsh/face-detect-opencv.git`.
* `cd face-detect-opencv' 
* `python main.py`

### Issue with cloning into docker
* If you have issues cloning into docker use wget to get the files `wget https://github.com/cyberutkarsh/face-detect-opencv/archive/master.zip`
* `unzip master.zip`
* `cd face-detect-opencv-master`
* `python main.py`
