import time

curr_time = time.time()

while True:
    instant_time = time.time()
    elapsed= instant_time - curr_time
    print(elapsed)