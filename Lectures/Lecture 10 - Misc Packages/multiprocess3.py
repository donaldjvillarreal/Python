import multiprocessing
import time

def worker():
    print(queue.get())
    print(queue.get())
    queue.put(5)
        
process = multiprocessing.Process(target=worker)
queue = multiprocessing.Queue()
queue.put(4)
queue.put(7)
process.start()
time.sleep(1)
print(queue.get())