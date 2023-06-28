number_map = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen'
}

tens_map = {
    '2': 'twenty',
    '3': 'thirty',
    '4': 'forty',
    '5': 'fifty',
    '6': 'sixty',
    '7': 'seventy',
    '8': 'eighty',
    '9': 'ninety'
}

def to_words(n):
    words = ''
    if n >= 100:
        words += number_map[str(n // 100)] + 'hundred'
    
    if (n % 100) >= 20:
        words += 'and' + tens_map[str((n % 100) // 10)] if len(words) > 0 else tens_map[str((n % 100) // 10)]
    elif (n % 100) >= 10:
        words += 'and' + number_map[str((n % 100))] if len(words) > 0 else number_map[str((n % 100))]

    if (n % 10) > 0 and not ((n % 100) < 20 and (n % 100) >= 10):
        words += 'and' + number_map[str(n % 10)] if 'and' not in words and 'hundred' in words else number_map[str(n % 10)]

    return words

count = 0
for i in range(1, 1000):
    w = to_words(i)
    print(i, w)
    count += len(w)

count += len('onethousand')

print(count)