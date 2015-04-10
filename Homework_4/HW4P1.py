import datetime
import time

def time_print (date_list):
	date_list = sorted(date_list)
	num_items = len(date_list)
	i=1
	for date_item in date_list:
		while datetime.datetime.now() < date_item:
			time.sleep(1)
		print ("Datetime " + str(i) + " of " + str(num_items) + " reached.")
		i+=1
	print("All dates have been printed")

userdates = [datetime.datetime(2015, 3, 23, 9, 36, 33), datetime.datetime(2015, 3, 23, 9, 36, 55), datetime.datetime(2015, 3, 23, 9, 36, 8)]
time_print(userdates)