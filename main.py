import Queue
import threading
import time
import os
from helpers.FaceDetectHelpers import *

#constants
exitFlag = 0
#image path
PATH = 'data/'

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
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

threadList = ["Thread-1", "Thread-2", "Thread-3"]
queueLock = threading.Lock()
workQueue = Queue.Queue(37601)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

#Loop through all images in the data directory and Fill the queue
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