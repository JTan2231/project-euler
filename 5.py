import concurrent.futures
import os

primes = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

n = 2520
minN = 0
stopFlag = False

def div_check(n, primes):
    global minN
    global stopFlag
    
    print('checking:', n, ', ', '                  ', end='\r')
    
    res = 0
    for p in primes:
        res = n % p
        if res != 0:
            return

    minN = n

workers = min(32, (os.cpu_count() or 1) + 4)
pool = concurrent.futures.ThreadPoolExecutor()

while not stopFlag:
    print('checking:', n, ', ', '                  ', end='\r')
    for i in range(workers):
        pool.submit(div_check(n + (i * 2), primes))

    n += workers * 2

print('                                                   ')
print('final answer:', minN)