"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here

    for item in items:
        key = str(item) # Convert the item into a string and use it as a key

        if key in frequencies:
            frequencies[key] += 1 # Increment value if the key already exists
        else:
            frequencies[key] = 1 # Set value to 1 if the key is new

    return frequencies
