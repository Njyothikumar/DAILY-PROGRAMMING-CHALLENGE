def first_element_k_times(arr, k):
    count_map = {}
    for num in arr:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    for num in arr:
        if count_map[num] == k:
            return num
    
    return -1

print(first_element_k_times([3, 1, 4, 4, 5, 2, 6, 1, 4], 2)) 
print(first_element_k_times([2, 3, 4, 2, 2, 5, 5], 2))
print(first_element_k_times([1, 1, 1, 1], 1))  
print(first_element_k_times([10], 1))  
print(first_element_k_times([6, 6, 6, 6, 7, 7, 8, 8, 8], 3)) 
