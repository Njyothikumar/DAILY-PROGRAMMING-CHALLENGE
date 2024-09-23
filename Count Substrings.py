def count_substrings_with_k_distinct(s: str, k: int):
    def count_at_most(k: int) -> int:
        if k == 0:
            return 0
        
        count = 0
        char_map = {}
        start = 0
        
        for end in range(len(s)):
            char_map[s[end]] = char_map.get(s[end], 0) + 1
            
            while len(char_map) > k:
                char_map[s[start]] -= 1
                if char_map[s[start]] == 0:
                    del char_map[s[start]]
                start += 1
            
            count += (end - start + 1)
        
        return count
    
    if k > len(s):
        return 0
    
    return count_at_most(k) - count_at_most(k - 1)

print(count_substrings_with_k_distinct("pqpqs", 2))  
print(count_substrings_with_k_distinct("aabacbebebe", 3))  
print(count_substrings_with_k_distinct("a", 1))  
print(count_substrings_with_k_distinct("abc", 3))  
print(count_substrings_with_k_distinct("abc", 2))  
