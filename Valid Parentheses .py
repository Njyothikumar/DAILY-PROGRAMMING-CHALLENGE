def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map.values():  
            stack.append(char)
        elif char in bracket_map.keys(): 
            if not stack or stack[-1] != bracket_map[char]:
                return False  
            stack.pop() 
        else:
            return False 
    
    return len(stack) == 0  
print(isValid("()"))      
print(isValid("([)]"))     
print(isValid("[{()}]"))   
print(isValid(""))         
print(isValid("{[}"))   
