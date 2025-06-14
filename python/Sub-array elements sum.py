# https://www.codewars.com/kata/5b5e0ef007a26632c400002a/train/python

def elements_sum(arr, d):
    result = 0
    n = len(arr)
    for subarr in range(n):
        index = n - subarr - 1
        if len(arr[subarr]) > index:
            result += arr[subarr][index]
        else:
            result += d
    return result
