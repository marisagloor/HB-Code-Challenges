"""Find window of time when most authors were active.

For example::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, and Carol were all active then).

If there's more than one period, find the earliest::

    >>> data = [
    ...    ('Alice', 1901, 1950),
    ...    ('Bob',   1920, 1960),
    ...    ('Carol', 1908, 1945),
    ...    ('Dave',  1951, 1960),
    ...    ('Eve',   1955, 1985),
    ... ]

    >>> most_active(data)
    (1920, 1945)

(Alice, Bob, Carol were active 1920-1945. Bob, Dave, and Eve were active 1951-1960.
Since there's a tie, the first was returned)
"""


def most_active(bio_data):
    """Find window of time when most authors were active."""
    inds_to_check = [0]
    checked = {0}
    poss = {}
    while inds_to_check:
        count = 0
        ind = inds_to_check.pop()
        low = bio_data[ind][1]
        high = bio_data[ind][2]
        for i, auth in enumerate(bio_data):
            if (auth[1] <= low & auth[2] > low) | (auth[2] >= high & auth[1] < high) | (auth[1] > low & auth[2] < high):
                count += 1
            if high > auth[1] > low:
                low = auth[1]
            if high > auth[2] > low:
                high = auth[2]
            if (auth[2] < low < high | auth[1] > high > low) & (not i in checked):
                inds_to_check.append(i)
                checked.append(i)
        if count in poss.keys():
            if low < poss[count][0]:
                poss[count] = (low, high)
        else:
            poss[count] = (low, high)

        return poss[max(poss.keys())]
        


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")