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

    #create minefield for year 1900 - 1999
    century = [0] * 100

    #Add 1 in every year in century when someone is active
    for person, start, end in bio_data:
        for year in range(start, end+1):
            century[year-1900] += 1

    #find time period when most authors were active
    best = 0
    in_best_time = True
    best_start_time = 0
    best_end_time = 100

    for year, num_active in enumerate(century):
        #replace best with active year if greater
        if num_active > best: 
            best = num_active
            in_best_time = True
            best_start_time = year

        elif num_active < best and in_best_time: 
            #no longer in best time period, find end
            best_end_time = year - 1
            in_best_time = False

    return (best_start_time + 1900, best_end_time + 1900)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
