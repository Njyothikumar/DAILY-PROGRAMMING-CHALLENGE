def longest_palindrome(s: str):
    if len(s) == 0:
        return ""

    start, end = 0, 0

    def expand_around_center(left: int, right: int) -> None:
        nonlocal start, end
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if (right - left - 1) > (end - start):
            start = left + 1
            end = right - 1

    for i in range(len(s)):
        expand_around_center(i, i)
        expand_around_center(i, i + 1)

    return s[start:end + 1]

print(longest_palindrome("babad"))  
print(longest_palindrome("cbbd"))   
print(longest_palindrome("a"))      
print(longest_palindrome("aaaa"))   
print(longest_palindrome("abc"))   
