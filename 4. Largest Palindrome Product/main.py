# Shreyas Poyrekar
# 07/1/2020
# problem: Largest palindrome product (Project Euler)
# Find the largest palindrome made from the product of two 3-digit numbers.
import time

#returns a list of all digits in of a integer
def int_list(n):
    ret = []
    while n!=0:
        ret.insert(0,n%10)
        n=int(n/10)
    return ret

#recursive function to check if a number is palindrome or not
def is_palindrome(lst,start,end):
    if( start >= end):
        return True
    if(lst[start] == lst[end]):
        return is_palindrome(lst,start+1,end-1)
    else:
        return False

"""
    i = 1000 - a
    j = 1000 - b
    num = i*j

    (a + 1) = 1001 - i
    (b + 1) = 1001 - j
    
    1000000 - 1000(a+b) + ab

    100000x + 10000y + 1000z + 100z +10y + x = 1000001x + 10010y + 1010z
    assumed ab is a 3 digit number equal to shown below
    100z + 10y + x = ab
    1000(100x + 10y + z) = 1000(1000 - (a+b))

    99z - 99x = ab + (a+b) - 1000
    z - x = 1/99(ab + a + b - 10) - 990/99 
    z - x = 1/99(ab + a + b - 10) - 10
    
    11(9p + 1) = (a+1)(b+1)
    11(9p + 1) = (1001 - i) * (1001 - j)
    1001 - 11/(1001 - i) = j
    1001 - 110/(1001 - i) = j
    and so on
    assumed  p goes from 0 to 9
    p = (z-x) + 10
    
"""


def main():
    s_flag = False
    for p in range(0,10):
        if (s_flag):
            break
        n = (11*(9*p + 1))
        for i in range(999,n,-1):
            j = 1001 - n*(1001 - i)
            num = i*j
            lst = int_list(num)
            if (is_palindrome(lst,0,len(lst)-1)):
                print("The largest palindrome made from the product of two 3-digit numbers is " + str(num))
                s_flag = True
                break

    
if __name__=="__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
