
def even_numbers(arr,n):
    list = [] # 2,6,8 ,      2
    for i in arr :
        if i % 2 == 0 :
            list.append(i)
         
    return list[-n:]

