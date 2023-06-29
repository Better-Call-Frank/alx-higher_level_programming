#!/usr/bin/python3

def best_score(a_dictionary):
    # Initialize variables to store the maximum score and corresponding key
    max_score = None
    max_key = None

    # Iterate over the key-value pairs in the dictionary
    for key, value in a_dictionary.items():
        # Check if the value is an integer and larger than the current maximum score
        if isinstance(value, int) and (max_score is None or value > max_score):
            max_score = value
            max_key = key

    return max_key
