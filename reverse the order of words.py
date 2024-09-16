def reverse_words(s: str) -> str:
    words = s.strip().split()
    
    reversed_words = words[::-1]
    
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

if __name__ == "__main__":
    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
        "    ",
        "word"
    ]

    for case in test_cases:
        result = reverse_words(case)
        print(f"Input: \"{case}\"")
        print(f"Output: \"{result}\"")
        print()
