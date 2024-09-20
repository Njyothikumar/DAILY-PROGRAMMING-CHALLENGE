def permute_unique(s: str):
    s = sorted(s)
    results = []
    
    def backtrack(path, used):
        if len(path) == len(s):
            results.append(''.join(path))
            return
        
        for i in range(len(s)):
            if used[i]:
                continue
            if i > 0 and s[i] == s[i - 1] and not used[i - 1]:
                continue
            
            used[i] = True
            path.append(s[i])
            backtrack(path, used)
            used[i] = False
            path.pop()
    used = [False] * len(s)
    backtrack([], used)
    
    return results

print(permute_unique("abc"))
print(permute_unique("aab"))  
print(permute_unique("aaa"))  
print(permute_unique("a"))    
print(permute_unique("abcd"))  
