def pad(n):
    if len(str(n)) < 4:
        return str('0' * (4 - len(str(n))) + str(n))
    return str(n)


def sort_asc(n):
    return pad(''.join(sorted(str(n))))


def sort_desc(n):
    return pad(''.join(reversed(sort_asc(n))))


def kaprekar_subtract(n):
    x = int(sort_desc(n))
    y = int(sort_asc(n))
    if x == 0 and y == 0:
        print(f'Something went wrong')
        exit(1)
    if x > y:
        return x - y
    return y - x


def kaprekar(n):
    i = 0
    while int(n) != 6174:
        i = i + 1
        n = kaprekar_subtract(n)
    return i

with open('./iters.txt', 'w+', encoding='utf8') as file:
    for i in range(1, 9999):
        if len(set(pad(i))) == 1:
            continue  # Requires 2 different digits
        iters = kaprekar(pad(i))
        msg = f'solved {i} in {iters} iterations'
        print(msg)
        file.write(msg + '\n')