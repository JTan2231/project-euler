import math

def is_prime(n):
    if n % 2 == 0:
        return 0

    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        if n % i == 0:
            return 0
        
    return n

total = 2
for i in range(3, 2 * 10**6):
    total += is_prime(i)
    
print(total)