from collections import Counter

def duplicates(array: list) -> list: 
    """Given an array of objects, returns an array of objects that are duplicated
    in the order that they first appear."""

    # Insertion order for dicts is preserved in python 3.7, counter extends a dict
    counter = Counter(array)
    return [element for element in counter.keys() if counter[element] > 1]
