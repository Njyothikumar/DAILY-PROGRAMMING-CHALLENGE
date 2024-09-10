def find_missing_numbers(arr):
    if not arr:
        raise ValueError("Array cannot be empty")
    n = len(arr) + 2  
    present_numbers = set(arr)
    missing_numbers = [num for num in range(1, n + 1) if num not in present_numbers]
    
    return missing_numbers
arr = [1, 2, 4, 6, 7, 10]
missing_numbers = find_missing_numbers(arr)
print("Missing numbers:", missing_numbers)
