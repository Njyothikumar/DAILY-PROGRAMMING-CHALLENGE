def longestCommonPrefix(string):
    if not string:
        return ""
    prefix = string[0]
    for s in string[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return""
    return prefix
if __name__ == "__main__":
    print(longestCommonPrefix(["flower","float","fligh"]))
        print(longestCommonPrefix(["dog", "racecar", "car"])) 
    print(longestCommonPrefix(["apple", "ape", "april"]))    
    print(longestCommonPrefix([""]))                        
    print(longestCommonPrefix(["alone"]))       
