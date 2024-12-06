def intersection(list_a, list_b):
    # Convert lists to sets and find the intersection
    set_a = set(list_a)
    set_b = set(list_b)
    
    # Return the sorted list of intersection elements (no duplicates)
    return list(set_a & set_b)  # '&' is the set intersection operator

# Example usage
list_a = [4, 9, 5]
list_b = [9, 4, 9, 8, 4]
result = intersection(list_a, list_b)
print(result)  # Output: [4, 9]
