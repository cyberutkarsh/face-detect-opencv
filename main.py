#Main File - Multithreaded queue based implementation of OpenCV based human facial detection.
#To Run: python main.py

import Queue
import threading
import time
import os
from helpers.FaceDetectHelpers import *

#constants
exitFlag = 0
#image path
PATH = 'data/'
#Define Queue Size based on the number of input images
QUEUE_SIZE=112

#Define a new subclass of the Thread class
#and Override the __init__ function
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_image_queue(self.name, self.q)
        print "Exiting " + self.name

#classify each image through multiple classifiers accessing
#them in the synchronized image queue
def process_image_queue(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            imagename = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, imagename)
            #classifier 1
            classify_frontface(PATH + imagename)
            #classifier 2
            classify_frontface_alternate1(PATH + imagename)
            #classifier 3
            classify_frontface_alternate2(PATH + imagename)
            #classifier 4
            classify_frontalface_alt_tree(PATH + imagename)
            #classifier 5
            classify_profileface(PATH + imagename)
        else:
            queueLock.release()
        time.sleep(1)

#we'll start with 3 threads, this can be bumped up based 
#on your system resource profile
threadList = ["Thread-1", "Thread-2", "Thread-3"]
queueLock = threading.Lock()
workQueue = Queue.Queue(QUEUE_SIZE)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

#Loop through all images in the data directory and Fill the queue
#to create a workload for the threads
queueLock.acquire()
for imagename in os.listdir(PATH):
    workQueue.put(imagename)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread"