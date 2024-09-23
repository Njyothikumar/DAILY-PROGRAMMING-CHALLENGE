def length_of_longest_substring(s: str):
    char_index = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)
        
        char_index[s[end]] = end
        
        max_length = max(max_length, end - start + 1)
    
    return max_length
print(length_of_longest_substring("abcabcbb")) 
print(length_of_longest_substring("bbbbb"))     
print(length_of_longest_substring("pwwkew"))    
print(length_of_longest_substring("abcdefgh"))   
print(length_of_longest_substring("a"))         
