import datetime
import time

print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.utcnow())
print(datetime.datetime.utcfromtimestamp(time.time()))
print(datetime.datetime.now().timestamp())