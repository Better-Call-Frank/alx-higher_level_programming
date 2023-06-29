#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate over each element in the input list
    for element in my_list:
        # Check if the element is an integer and add it to the set
        if isinstance(element, int):
            unique_integers.add(element)

    # Calculate the sum of the unique integers
    sum_unique = sum(unique_integers)

    return sum_unique
