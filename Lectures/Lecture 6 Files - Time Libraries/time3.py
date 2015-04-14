import time

def some_function_we_want_to_time():
    j = 0
    for i in range(10000000):
        j = i



start = time.process_time()
some_function_we_want_to_time()
end = time.process_time()

print(end - start)
