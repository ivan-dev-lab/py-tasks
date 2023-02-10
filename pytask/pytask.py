#-*-coding:cp1251-*-


#algoritm of binary search
from random import randint
def binary_search():
    n = randint(1,100)
    nums = [el for el in range(1,101)]
    l, m, h = 0, 0, 0
    print(f"the desired number: {n}")
    while True:
        print(f"the average num = {m}\n\nlist of data = {nums}")
        l,m,h = nums[0],nums[(len(nums)//2)-1],nums[(len(nums))-1]
        if n == m:
            break
        elif n>m:
            nums = [el for el in range(m,h+1)]
        else:
            nums = [el for el in range(l,m+1)]
        
    print(f"num finded!, the desired num = {n}")
#binary_search()
