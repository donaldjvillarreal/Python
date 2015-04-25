import multiprocessing
import time

class Worker(multiprocessing.Process):
    def run(self):
        print("Started worker: %s" % self.name)
        time.sleep(1)
        print("Ended worker: %s" % self.name)
        
worker1 = Worker()
worker2 = Worker()
worker1.start()
worker2.start()
