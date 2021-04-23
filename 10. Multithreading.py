####$$$~~~~~~~ Multithreading  ~~~~~~~~~$$$####

""" The ability of a process to execute multiple threads parallelly is called
multithreading. Ideally, multithreading can significantly improve the
performance of any program. And Python multithreading mechanism is pretty
user-friendly  """

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import threading
##
##def delayed():
##    print("I am printed after 5 seconds!")
##
##thread = threading.Timer(5, delayed)
##thread.start()

        #~~~~~Output
        ##I am printed after 5 seconds!


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import threading
##def worker():
##    """thread worker function"""
##    print('Worker')
##    return

##threads = []
##for i in range(5):
##    t = threading.Thread(target=worker)
##    threads.append(t)
##    t.start()

        #~~~~Output
        ##WorkerWorkerWorkerWorkerWorker


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import time
##from threading import Thread
##
##def sleepMe(i):
##    print("Thread %i going to sleep for 5 seconds." % i)
##    time.sleep(5)
##    print("Thread %i is awake now." % i)
##
##for i in range(10):
##    th = Thread(target=sleepMe, args=(i, ))
##    th.start()

        #~~~~~Output
        ##Thread 0 going to sleep for 5 seconds.Thread 1 going to sleep for 5 seconds.Thread
        ##2 going to sleep for 5 seconds.Thread 3 going to sleep for 5 seconds.Thread 4
        ##going to sleep for 5 seconds.Thread 5 going to sleep for 5 seconds. Thread 6
        ##going to sleep for 5 seconds.Thread 7 going to sleep for 5 seconds.Thread 8
        ##going to sleep for 5 seconds.Thread 9 going to sleep for 5 seconds.
        ##
        ##Thread 0 is awake now.
        ##Thread 1 is awake now.Thread 2 is awake now.
        ##
        ##Thread 3 is awake now.Thread 4 is awake now.
        ##
        ##Thread 5 is awake now.Thread 6 is awake now.
        ##
        ##Thread 7 is awake now.
        ##Thread 8 is awake now.
        ##Thread 9 is awake now.


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##from _thread import start_new_thread
##from time import sleep
##
##from _thread import start_new_thread
##from time import sleep
##
##threadId = 1 # thread counter
##waiting = 2 # 2 sec. waiting time

##def factorial(n):
##    global threadId
##    rc = 0
##    
##    if n < 1:   # base case
##        print("{}: {}".format('\nThread', threadId ))
##        threadId += 1
##        rc = 1
##    else:
##        returnNumber = n * factorial( n - 1 )  # recursive call
##        print("{} != {}".format(str(n), str(returnNumber)))
##        rc = returnNumber
##    return rc

##start_new_thread(factorial, (5, ))
##start_new_thread(factorial, (4, ))
##
##print("Waiting for threads to return...")
##sleep(waiting)

        #~~~~Output
        ##Waiting for threads to return...
        ##Thread: 1
        ##Thread: 1
        ##1 != 11 != 1
        ##2 != 22 != 2
        ##3 != 63 != 6
        ##4 != 244 != 24
        ##5 != 120


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import threading
##import datetime
##
##class myThread (threading.Thread):
##    def __init__(self, name, counter):
##        threading.Thread.__init__(self)
##        self.threadID = counter
##        self.name = name
##        self.counter = counter
##    def run(self):
##        print("\nStarting " + self.name)
##        print_date(self.name, self.counter)
##        print("Exiting " + self.name)

##def print_date(threadName, counter):
##    datefields = []
##    today = datetime.date.today()
##    datefields.append(today)
##    print("{}[{}]: {}".format( threadName, counter, datefields[0] ))

### Create new threads
##thread1 = myThread("Thread", 1)
##thread2 = myThread("Thread", 2)
##
### Start new Threads
##thread1.start()
##thread2.start()
##
##thread1.join()
##thread2.join()
##print("\nExiting the Program!!!")

        #~~~~Output
        ##Starting Thread
        ##Starting Thread
        ##Thread[1]: 2019-10-27Thread[2]: 2019-10-27
        ##Exiting ThreadExiting Thread
        ##Exiting the Program!!!


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import threading
##import datetime
##
##exitFlag = 0
##
##class myThread (threading.Thread):
##    def __init__(self, name, counter):
##        threading.Thread.__init__(self)
##        self.threadID = counter
##        self.name = name
##        self.counter = counter
##    def run(self):
##        print("\nStarting " + self.name)
##        # Acquire lock to synchronize thread
##        threadLock.acquire()
##        print_date(self.name, self.counter)
##        # Release lock for the next thread
##        threadLock.release()
##        print("Exiting " + self.name)
##
##def print_date(threadName, counter):
##    datefields = []
##    today = datetime.date.today()
##    datefields.append(today)
##    print("{}[{}]: {}".format( threadName, counter, datefields[0] ))
##
##threadLock = threading.Lock()
##threads = []
##
### Create new threads
##thread1 = myThread("Thread", 1)
##thread2 = myThread("Thread", 2)
##
### Start new Threads
##thread1.start()
##thread2.start()
##
### Add threads to thread list
##threads.append(thread1)
##threads.append(thread2)
##
### Wait for all threads to complete
##for thread in threads:
##    thread.join()
##
##print("\nExiting the Program!!!")


        #~~~~Output
        ##Starting Thread
        ##Starting Thread
        ##Thread[1]: 2019-10-27
        ##Thread[2]: 2019-10-27Exiting Thread
        ##Exiting Thread
        ##Exiting the Program!!!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

""" The logging module supports embedding the thread name in every log message
using the formatter code %(threadName)s. Including thread namesin log messages
makes it easier to trace those messages back to their source. """

##import logging
##import threading
##import time
##
##def thread_function(name):
##    logging.info("Thread %s: starting", name)
##    time.sleep(2)
##    logging.info("Thread %s: finishing", name)
##
##if __name__ == "__main__":
##    format = "%(asctime)s: %(message)s"
##    logging.basicConfig(format=format, level=logging.INFO,
##                        datefmt="%H:%M:%S")
##
##    threads = list()
##    for index in range(3):
##        logging.info("Main    : create and start thread %d.", index)
##        x = threading.Thread(target=thread_function, args=(index,))
##        threads.append(x)
##        x.start()
##
##    for index, thread in enumerate(threads):
##        logging.info("Main    : before joining thread %d.", index)
##        thread.join()
##        logging.info("Main    : thread %d done", index)

        #~~~~Output
        ##20:33:07: Main    : create and start thread 0.
        ##20:33:07: Thread 0: starting
        ##20:33:07: Main    : create and start thread 1.
        ##20:33:07: Thread 1: starting
        ##20:33:07: Main    : create and start thread 2.
        ##20:33:07: Thread 2: starting
        ##20:33:07: Main    : before joining thread 0.
        ##20:33:09: Thread 0: finishing
        ##20:33:09: Thread 1: finishing
        ##20:33:09: Main    : thread 0 done
        ##20:33:09: Thread 2: finishing
        ##20:33:09: Main    : before joining thread 1.
        ##20:33:09: Main    : thread 1 done
        ##20:33:09: Main    : before joining thread 2.
        ##20:33:09: Main    : thread 2 done


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import threading
##def worker(num):
##    """thread worker function"""
##    print('Worker: %s' % num)
##    return
##
##threads = []
##for i in range(5):
##    t = threading.Thread(target=worker, args=(i,))
##    threads.append(t)
##    t.start()

        #~~~~~Output
        ##Worker: 0Worker: 1Worker: 2Worker: 3Worker: 4


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import threading
##import time
##
##def worker():
##    print(threading.currentThread().getName(), 'Starting')
##    time.sleep(2)
##    print(threading.currentThread().getName(), 'Exiting')
##
##def my_service():
##    print(threading.currentThread().getName(), 'Starting')
##    time.sleep(3)
##    print(threading.currentThread().getName(), 'Exiting')
##
##t = threading.Thread(name='my_service', target=my_service)
##w = threading.Thread(name='worker', target=worker)
##w2 = threading.Thread(target=worker) # use default name

##w.start()
##w2.start()
##t.start()

        #~~~~~Output
        ##workerThread-1my_service
        ##>>>    StartingStartingStarting
        ##workerThread-1  ExitingExiting
        ##my_service Exiting



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import logging
##import threading
##import time
##
##logging.basicConfig(level=logging.DEBUG,
##                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',)
##
##def worker():
##    logging.debug('Starting')
##    time.sleep(2)
##    logging.debug('Exiting')
##
##def my_service():
##    logging.debug('Starting')
##    time.sleep(3)
##    logging.debug('Exiting')
##
##t = threading.Thread(name='my_service', target=my_service)
##w = threading.Thread(name='worker', target=worker)
##w2 = threading.Thread(target=worker) # use default name
##
##w.start()
##w2.start()
##t.start()


#~~~~~Output
##[DEBUG] (worker    ) Starting
##[DEBUG] (Thread-1  ) Starting
##[DEBUG] (my_service) Starting
##[DEBUG] (worker    ) Exiting
##[DEBUG] (Thread-1  ) Exiting
##[DEBUG] (my_service) Exiting


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

##import threading
##for thread in threading.enumerate():
##    print("Thread name is %s." % thread.getName())

        #~~~~~Output
        ##Thread name is MainThread.
        ##Thread name is SockThread.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~Output





