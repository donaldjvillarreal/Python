import time

start_time = time.time()
start_process_time = time.process_time()

time.sleep(1)

end_time = time.time()
end_process_time = time.process_time()

print(end_time - start_time)
print(end_process_time - start_process_time)
