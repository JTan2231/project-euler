def collatz(n):
    length = 0
    while n > 1:
        length += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    return length

i = int(1e6 - 1)
longest = 1
number = 0
while i > 1:
    c = collatz(i)
    if c > longest:
        longest = c
        number = i

    print(f'{i}, {longest}, {number}                            ', end='\r')

    i -= 1

print('DONE')