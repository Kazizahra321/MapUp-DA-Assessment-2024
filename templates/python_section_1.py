def reverse_by_n_elements(lst, n):
    result = []
    
    # Iterate over the list in steps of n
    for i in range(0, len(lst), n):
        group = lst[i:i + n]  # Get the next group of n elements
        
        # Reverse the current group manually
        reversed_group = []
        for j in range(len(group)-1, -1, -1):
            reversed_group.append(group[j])
        
        # Add the reversed group to the result
        result.extend(reversed_group)
    
    return result

# Example usage:
print(reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [3, 2, 1, 6, 5, 4, 8, 7]
print(reverse_by_n_elements([1, 2, 3, 4, 5], 2))           # Output: [2, 1, 4, 3, 5]
print(reverse_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4)) # Output: [40, 30, 20, 10, 70, 60, 50]
def group_strings_by_length(lst):
    length_dict = {}
    
    # Iterate over each string in the list
    for word in lst:
        length = len(word)  # Get the length of the string
        
        # Add the word to the appropriate list in the dictionary
        if length not in length_dict:
            length_dict[length] = [word]  # Create a new list if key doesn't exist
        else:
            length_dict[length].append(word)  # Append to the existing list
    
    # Return the dictionary sorted by key (length)
    return dict(sorted(length_dict.items()))

# Example usage:
print(group_strings_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
# Output: {3: ['bat', 'car', 'dog'], 4: ['bear'], 5: ['apple'], 8: ['elephant']}

print(group_strings_by_length(["one", "two", "three", "four"]))
# Output: {3: ['one', 'two'], 4: ['four'], 5: ['three']}
