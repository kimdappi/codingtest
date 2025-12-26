def solution(arr, idx):
    i = idx
    while i < len(arr):
        if arr[i] == 1:
            return i
        i += 1
    return -1
