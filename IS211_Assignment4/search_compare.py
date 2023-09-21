import time
import random


def sequential_search(a_list, item):
    start_time = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = time.time()
    total_time = end_time - start_time

    return total_time, found


def ordered_sequential_search(a_list, item):
    a_list.sort()

    start_time = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = time.time()
    total_time = end_time - start_time

    return total_time, found


def binary_search_iterative(a_list, item):
    a_list.sort()

    start_time = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = time.time()
    total_time = end_time - start_time

    return total_time, found


def binary_search_recursive(a_list, item):
    a_list.sort()

    start_time = time.time()
    found = False

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2

        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                total_time, found = binary_search_recursive(a_list[:midpoint], item)
            else:
                total_time, found = binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = time.time()
    total_time = end_time - start_time

    return total_time, found


def gen_random_list(size):
    return random.sample(range(0, size), size)


def main():

    tests = [500, 1000, 10000]
    results = {
        'Sequential Search': 0.0,
        'Ordered Sequential Search': 0.0,
        'Binary Search Iterative': 0.0,
        'Binary Search Recursive': 0.0
    }

    for test in tests:
        i = 0

        while i < 100:
            test_list = gen_random_list(test)
            results['Sequential Search'] += sequential_search(test_list, -1)[0]
            results['Ordered Sequential Search'] += ordered_sequential_search(test_list, -1)[0]
            results['Binary Search Iterative'] += binary_search_iterative(test_list, -1)[0]
            results['Binary Search Recursive'] += binary_search_recursive(test_list, -1)[0]
            i += 1

        print("Search results for list of size %s items:" % test)
        for key, value in results.items():
            print("%s took %10.7f seconds to run, on average." % (key, (value / 100)))
        print("\n")


if __name__ == '__main__':
    main()