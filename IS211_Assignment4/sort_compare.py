
import time
import random


def insertion_sort(alist):
    start_time = time.time()

    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue

    end_time = time.time()
    total_time = end_time - start_time

    return total_time, alist


def shell_sort(alist):
    start_time = time.time()

    sublistcount = len(alist) // 2

    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)

        sublistcount = sublistcount // 2

    end_time = time.time()
    total_time = end_time - start_time

    return total_time, alist


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


def python_sort(alist):
    start_time = time.time()

    alist.sort()

    end_time = time.time()
    total_time = end_time - start_time

    return total_time, alist


def gen_random_list(size):
    return random.sample(range(0, size), size)


def main():

    tests = [500, 1000, 10000]
    results = {
        'Insertion Sort': 0.0,
        'Shell Sort': 0.0,
        'Python Sort': 0.0
    }

    for test in tests:
        i = 0

        while i < 100:
            test_list = gen_random_list(test)
            results['Insertion Sort'] += insertion_sort(test_list)[0]
            results['Shell Sort'] += shell_sort(test_list)[0]
            results['Python Sort'] += python_sort(test_list)[0]
            i += 1

        print("Sort results for list of size %s items:" % test)
        for key, value in results.items():
            print("%s took %10.7f seconds to run, on average." % (key, (value / 100)))
        print("\n")


if __name__ == '__main__':
    main()