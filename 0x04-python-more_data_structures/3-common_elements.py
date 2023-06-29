#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Create an empty set to store the common elements
    common_elements_set = set()

    # Iterate over each element in the first set
    for element in set_1:
        # Check if the element is also present in the second set
        if element in set_2:
            common_elements_set.add(element)

    return common_elements_set
