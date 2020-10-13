import random

f = open('data.txt', 'r', encoding="UTF-8")
arr = []
for eachLine in f:
    arr.append(eachLine)


def RandomHoroscope():
    try:
        b = int(random.randint(0, len(arr) - 1))
        str = arr[b]
        arr.pop(b)
    except ValueError:
        print('null')
    return str

