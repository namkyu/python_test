

import thread
import time
import threading

def print_time(threadName, delay):
	threadLock.acquire()
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print("%s: %s" % (threadName, time.ctime(time.time())))

	threadLock.release()

try:
	threadLock = threading.Lock()
	thread.start_new_thread(print_time, ("Thread-1", 1))
	thread.start_new_thread(print_time, ("Thread-2", 1))

except:
	print("Error")

while 1:
	pass