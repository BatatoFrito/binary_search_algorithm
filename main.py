'''

This program is a binary search algorithm

'''

from typing import Iterable
    
def binary_search(array_search: Iterable, value_search: str | int, print_process: bool) -> int:
    # Sorting the iterable and getting length values 
    array_search.sort()
    result = None

    # Type checking
    try:
        value_search = float(value_search)
    except(ValueError):
        pass

    try:
        value_search = int(value_search)
    except(ValueError):
        pass
    
    if type(value_search) != type(array_search[0]):            
        value_search = str(value_search)
    
    # Will slice the iterable in half until one element is left
    while True:
        array_len = -len(array_search)
        array_len_half = round(array_len/2)

        if print_process:
            print(array_search)

        # Checks if element is the right one
        if array_len == -1:
            if array_search[0] == value_search:
                result = 1
                break
            else:
                result = -1
                break

        value_compare = array_search[array_len_half]

        # Slicing
        if value_search < value_compare:
            array_search[array_len_half:] = []
        else:
            array_search[array_len:array_len_half] = []

    return result

if __name__ == '__main__':
    array_search = [3, 4, 40, 23, 12, 10, 2, 33, 2, 5]
    value_search = input()

    print(binary_search(array_search, value_search, True))