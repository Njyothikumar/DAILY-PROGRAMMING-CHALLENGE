def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    prefix_map = {0: [-1]} 
    results = []
    
    for i, num in enumerate(arr):
        prefix_sum += num
        
        if prefix_sum in prefix_map:
            for start_index in prefix_map[prefix_sum]:
                results.append((start_index + 1, i))
        
        if prefix_sum not in prefix_map:
            prefix_map[prefix_sum] = []
        
        prefix_map[prefix_sum].append(i)
    
    return results

print(find_zero_sum_subarrays([1, 2, -3, 3, -1, 2]))  
print(find_zero_sum_subarrays([4, -1, -3, 1, 2, -1])) 
print(find_zero_sum_subarrays([1, 2, 3, 4]))  
print(find_zero_sum_subarrays([0, 0, 0]))  
print(find_zero_sum_subarrays([-3, 1, 2, -3, 4, 0])) 
