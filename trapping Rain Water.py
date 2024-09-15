def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water_trapped = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1

    return water_trapped

if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 1, 1], 0),
        ([5], 0),
        ([2, 0, 2], 2),
        ([0, 0, 0, 0, 0], 0),  
        ([2, 1], 0),            
        ([1, 2, 3, 4, 5], 0),  
        ([5, 4, 3, 2, 1], 0)   
    ]

    for heights, expected in test_cases:
        result = trap(heights)
        print(f"Input: {heights} => Output: {result} (Expected: {expected})")
        assert result == expected, "Test failed!"
    
    print("All test cases passed!")
