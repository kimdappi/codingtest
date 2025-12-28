def solution(arr, flag):
    X = []

    for num, f in zip(arr, flag):
        if f:
            X.extend([num] * (num * 2))
        else:
            X = X[:-num]
            
    return X