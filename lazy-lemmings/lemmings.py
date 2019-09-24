"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, cafes):
    """Find longest distance between a hole and a cafe."""
    largest = 0
    if cafes[0] > largest:
        largest = cafes[0]

    if num_holes - 1 - cafes[-1] > largest:
        largest = num_holes - 1 - cafes[-1]

    if len(cafes) > 2:
        for i, cafe in enumerate(cafes[1:-1]):
            lower = int((cafe - cafes[i])/ 2)
            higher = int((cafes[i + 2] - cafe) / 2)
            if lower > largest:
                largest = lower
            if higher > largest:
                largest = higher
    else:
        mid = int((cafes[-1] - cafes[0])/2)
        if mid > largest:
            largest = mid
        
    return largest


def furthest_optimized(num_holes, cafes):
    largest = 0
    if cafes[0] > largest:
        largest = cafes[0]

    if num_holes - 1 - cafes[-1] > largest:
        largest = num_holes - 1 - cafes[-1]

    if len(cafes) > 2:
        for i, cafe in enumerate(cafes[1:-1]):
            lower = int((cafe - cafes[i])/ 2) 
            higher = int((cafes[i + 2] - cafe) / 2)
            if lower > largest:
                largest = lower
            if higher > largest:
                largest = higher
    else:
        mid = int((cafes[-1] - cafes[0])/2)
        if mid > largest:
            largest = mid

    return largest


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
