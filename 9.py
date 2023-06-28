import math

for b in range(100, 1000):
    for a in range(1, b):
        c = math.sqrt(a ** 2 + b ** 2)

        print(f'{a}, {b}, {c}                       ', end='\r')
        if a + b + c == 1000:
            print(a * b * c, '                                  ')
            exit(0)