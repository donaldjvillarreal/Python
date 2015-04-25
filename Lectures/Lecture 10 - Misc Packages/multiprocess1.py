import multiprocessing
import time

def worker():
    print('Started worker')
    time.sleep(1)
    print('Ended worker')

for i in range(5):
    process = multiprocessing.Process(target=worker)
    process.start()