#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    result = []

    # Iterate over each element in the input list
    for element in my_list:
        # If the element matches the search element, replace it with the new element
        if element == search:
            result.append(replace)
        else:
            result.append(element)

    return result
