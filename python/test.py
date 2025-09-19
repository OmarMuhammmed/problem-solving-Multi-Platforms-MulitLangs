import collections

str1 = "anagram"
str2 = "nagaram"

dic = {}
for i in str1:
    counter = 0
    if i in str1 :
        dic.setdefault(i,counter)
        counter+=1
    

print (dic)