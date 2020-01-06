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

    #declare start time for the window, set to the first start time in bio data
    start_time = bio_data[0][1]

    #declare end time for the window, set to the first end time in bio data
    end_time = bio_data[0][2]

    #loop through bio_data to find latest starting window for an author
    for bio in bio_data:

        if bio[1] > start_time:

            #replace start time if the author's start window is later
            start_time = bio[1]

        if bio[2] < end_time:

            #replace end time if the author's end window is earlier
            end_time = bio[2]

    return (start_time, end_time)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
