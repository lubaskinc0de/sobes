import random
import time

array = [
    random.randint(1, 100000000)
    for _ in range(1000000)
]


def qsort(arr):
    if len(arr) < 2:
        return arr

    low = []
    high = []
    equals = []
    anchor = random.choice(arr)  # O(n log n) anchor

    for el in arr:
        if el < anchor:
            low.append(el)
        if el > anchor:
            high.append(el)
        if el == anchor:
            equals.append(el)

    equals.append(anchor)

    return qsort(low) + equals[1:] + qsort(high)


start = time.perf_counter()
res = qsort(array)
perf = time.perf_counter() - start

print(f"Количество элементов в массиве: {len(array)}")
print(f"Затраченное время (в секундах): {perf}")

try:
    assert res == list(sorted(array))

    print("Тест: пройден")
except AssertionError:
    print("Тест: не пройден")