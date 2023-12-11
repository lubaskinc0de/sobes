import random
import time

search_array = list(sorted([
    random.randint(0, 100000000)
    for _ in range(1000000)
]))

search_query = random.choice(search_array)


def binary_search(array, query):
    top = len(array) - 1
    low = 0
    iterations = 0

    while low <= top:
        iterations += 1
        mid = (low + top) // 2

        if array[mid] == query:
            return mid, iterations
        if array[mid] < query:
            low = mid + 1
        else:
            top = mid - 1

    return None


start = time.perf_counter()
res, iteration = binary_search(search_array, search_query)
perf = time.perf_counter() - start

print(f"\nТребуется найти индекс значения: {search_query}")
print(f"Количество элементов в массиве: {len(search_array)}\n")
print(f"Затраченное количество итераций: {iteration}")
print(f"Затраченное время (в секундах): {perf}\n")
print(f"Индекс значения: {res}\n")

try:
    assert res == search_array.index(search_query)
    assert search_array[res] == search_query
    assert binary_search(search_array, -1) is None

    print("Тест: пройден")
except AssertionError:
    print("Тест: не пройден.")
