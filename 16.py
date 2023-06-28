import sys
sys.set_int_max_str_digits(0)

number = [int(digit) for digit in list(str(2 ** 1000))]
print(sum(number))