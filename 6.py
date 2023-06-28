import math

def is_prime(n):
    if n % 2 == 0:
        return 0

    for i in range(3, math.ceil(n ** 0.5) + 1, 2):
        if n % i == 0:
            return 0
        
    return 1

count = 6
n = 14
while count < 10001:
    count += is_prime(n)
    n += 1
    print(f'{count}, {n}                         ', end='\r')

print(f'{count}, {n - 1}                         ')