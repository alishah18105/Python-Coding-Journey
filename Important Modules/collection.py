import time

print("Start")
time.sleep(2)   # 2 seconds delay
print("End")

# Current timestamp
print("Timestamp:", time.time())

# Performance measure
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print("Execution time:", end - start)
