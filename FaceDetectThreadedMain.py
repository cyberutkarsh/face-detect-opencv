import threading
import time
import os
from helpers.FaceDetectHelpers import *

#constants
exitFlag = 0
#image path
PATH = 'data/'

class myThread (threading.Thread):    
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name        
    def run(self):
        print "Starting " + self.name
        start_classification(self.name)
        print "Exiting " + self.name

def start_classification(threadName):
    #Loop through all images in the data directory
    for imagename in os.listdir(PATH):
        if exitFlag:
            threadName.exit()
        
        print "%s: %s" % (threadName, time.ctime(time.time()))
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

# Create new threads
thread1 = myThread(1, "Thread-1")
thread2 = myThread(2, "Thread-2")

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"