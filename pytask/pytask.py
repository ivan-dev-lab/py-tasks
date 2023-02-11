#-*-coding:cp1251-*-


#binary search
from random import randint
def binary_search() -> int:
    n = randint(1,100)
    nums = [el for el in range(1,101)]
    l, m, h = 0, 0, 0
    print(f"the desired number: {n}")
    while True:
        #print(f"the average num = {m}\n\nlist of data = {nums}")
        l,m,h = nums[0],nums[(len(nums)//2)-1],nums[(len(nums))-1]
        if n == m:
            break
        elif n>m:
            nums = [el for el in range(m,h+1)]
        else:
            nums = [el for el in range(l,m+1)]
        
    return n
#print(f"num finded!, the desired num = {binary_search()}")


#finding the Fibonacci sequence
limit = int(input("up to what number is the sequence needed: "))
def find_Fib_seq () -> list:
    i = 0
    seq = [0,1]
    i = 0
    while len(seq) < limit:
        seq.append(seq[i]+seq[i+1])
        i+=1
    return seq
print(f"the sequence = {find_Fib_seq()}")


#next prime number
def find_next_prime_number ():
    ...