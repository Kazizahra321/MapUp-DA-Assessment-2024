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

def flatten_dict(nested_dict, parent_key='', sep='.'):
    items = {}

    for key, value in nested_dict.items():
        # Create a new key by appending the parent key and current key
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        
        if isinstance(value, dict):
            # If the value is a dictionary, recurse into it
            items.update(flatten_dict(value, new_key, sep=sep))
        elif isinstance(value, list):
            # If the value is a list, iterate through it
            for i, item in enumerate(value):
                # Create new key for each index
                index_key = f"{new_key}[{i}]"
                if isinstance(item, dict):
                    # Recurse into the dictionary if the item is a dictionary
                    items.update(flatten_dict(item, index_key, sep=sep))
                else:
                    # Otherwise, set the value directly
                    items[index_key] = item
        else:
            # For any other type, set the value directly
            items[new_key] = value
    
    return items

# Example usage:
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

flattened_dict = flatten_dict(nested_dict)
print(flattened_dict)
def generate_unique_permutations(nums):
    def backtrack(path, used):
        # If the current path has the same length as the input list, we found a permutation
        if len(path) == len(nums):
            result.append(path[:])  # Append a copy of the current permutation to the result
            return
        
        for i in range(len(nums)):
            if used[i]:  # If the number is already used in the current permutation, skip it
                continue
            
            # Skip duplicates: If the current number is the same as the previous one and the previous one was not used,
            # it means we are at the same level of recursion with the same number, which is not allowed.
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            
            used[i] = True  # Mark the number as used
            path.append(nums[i])  # Include the number in the current permutation
            
            backtrack(path, used)  # Recurse to generate permutations
            
            # Backtrack: Remove the last added number and mark it as unused
            path.pop()
            used[i] = False

    nums.sort()  # Sort the input to handle duplicates
    result = []
    used = [False] * len(nums)  # Track whether a number is used in the current permutation
    backtrack([], used)
    
    return result

# Example usage
input_list = [1, 1, 2]
unique_permutations = generate_unique_permutations(input_list)
print(unique_permutations)

import re

def find_all_dates(text):
    # Define a regex pattern for the specified date formats
    pattern = r'(\d{2}-\d{2}-\d{4}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2})'
    
    # Use re.findall to find all matches of the pattern in the input text
    dates = re.findall(pattern, text)
    
    return dates

# Example usage
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
found_dates = find_all_dates(text)
print(found_dates)

def rotate_matrix(matrix):
    n = len(matrix)
    
    # Step 1: Rotate the matrix by 90 degrees clockwise
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    # Step 2: Replace each element with the sum of its row and column, excluding itself
    final_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated_matrix[i])
            col_sum = sum(rotated_matrix[k][j] for k in range(n))
            final_matrix[i][j] = row_sum + col_sum - rotated_matrix[i][j]  # Exclude itself

    return final_matrix

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = rotate_matrix(matrix)
print(result)


