import datetime
import time

def wait_inc(x):
	new_time = datetime.datetime.now() + datetime.timedelta(seconds = x)
	while datetime.datetime.now() < new_time:
		time.sleep(1)
	print ("The system has waited " + str(x) + " seconds.")

x = input("How many seconds should the system wait?  ")
wait_inc(x)