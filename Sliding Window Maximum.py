from collections import deque

def sliding_window_maximum(arr, k):
    if not arr or k == 0:
        return []

    n = len(arr)
    max_in_windows = []
    deq = deque()

    for i in range(n):
        if deq and deq[0] < i - k + 1:
            deq.popleft()

        while deq and arr[deq[-1]] < arr[i]:
            deq.pop()

        deq.append(i)

        if i >= k - 1:
            max_in_windows.append(arr[deq[0]])

    return max_in_windows

# Example usage
print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))  
print(sliding_window_maximum([1, 5, 3, 2, 4, 6], 3))  
print(sliding_window_maximum([1, 2, 3, 4], 2))  
print(sliding_window_maximum([7, 7, 7, 7], 1)) 
