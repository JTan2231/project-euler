import math

def is_prime(n):
    if n % 2 == 0:
        return 0

    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        if n % i == 0:
            return 0
        
    return n

def sigma(n): 
    return sum(1 for d in range(1, n) if n % d == 0)

print(sigma(76576500))
exit()

i = 101
count = sigma(int(i * (i + 1) / 2))
stop = False
while not stop:
    print(f'{i}, {count}               ', end='\r')
    count = sigma(int(i * (i + 1) / 2))
    if count >= 500:
        stop = True

    i += 2

print(int(i * (i + 1) / 2))