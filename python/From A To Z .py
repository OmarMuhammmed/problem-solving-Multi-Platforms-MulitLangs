# https://www.codewars.com/kata/6512b3775bf8500baea77663/train/python


def gimme_the_letters(sp):
    result = ''
    for c in range(ord(sp[0]), ord(sp[2]) + 1):
        result += chr(c)
    return result
   

 
print(gimme_the_letters("a-z"))