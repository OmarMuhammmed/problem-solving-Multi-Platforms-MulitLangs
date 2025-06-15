# https://www.codewars.com/kata/559760bae64c31556c00006b/train/python


def climb(n):
    result = []
    while n > 1 :
        result.insert(0,n)
        n = n // 2 
    result.insert(0,n)    
    
    return result