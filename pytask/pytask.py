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
#limit = int(input("up to what number is the sequence needed: "))
def find_Fib_seq (l) -> list:
    i = 0
    seq = [0,1]
    i = 0
    while len(seq) < l:
        seq.append(seq[i]+seq[i+1])
        i+=1
    return seq
#print(f"the sequence = {find_Fib_seq(limit)}")


#next prime number
def find_next_prime_number ():
    n = int(input("enter number: "))
    while n!=0:
        s = 0
        for num in range(2,n+1):
            if n%num==0 and num!=n:
                s+=1
        if s==0:
            print("it is prime number")
        else:
            print("it is not prime number")
        n = int(input("enter number: "))
#find_next_prime_number()


#transfer from systems
#N = input("enter number from decimal to binary: ")
#N = input("enter number from binary to decimal: ")
def dec_to_bin (n: int) -> str:
    bin_list = []
    while n//2!=0:
        bin_list.append(n%2)
        n//=2
    bin_list.append(1)
    bin_list.reverse()
    bin_list = list(map(str,bin_list))
    return ''.join(bin_list)
def bin_to_dec (n: str) -> int: 
    bin_list = list(n)
    print(bin_list)
    bin_list.reverse()
    dec_int = 0
    for i,n in enumerate(bin_list):
        print(i,n)
        dec_int+=int(n)*(2**int(i))
    return dec_int
#print(dec_to_bin(int(N))) 
#print(bin_to_dec(N))


#finding factorial
#N = int(input("enter nuber for see his factorial: "))
def factorial (num: int) -> int:
    f = 1
    for n in range(1,num+1):
        f*=n
    return f
#print(factorial(N))