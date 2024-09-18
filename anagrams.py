def group_anagrams(strs): 
    anagram_dict = {}
     
    for s in strs: 
        key = ''.join(sorted(s))
         
        if key not in anagram_dict: 
            anagram_dict[key] = []
         
        anagram_dict[key].append(s)
     
    return list(anagram_dict.values())

# Test Cases
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  
print(group_anagrams([""]))  
print(group_anagrams(["a"]))  
print(group_anagrams(["abc", "bca", "cab", "xyz", "zyx", "yxz"]))    
print(group_anagrams(["abc", "def", "ghi"]))   
