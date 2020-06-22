# Shreyas Poyrekar
# 06/22/2020
# problem: 3 largest prime factor (Project Euler)
# finds the largest prime factor of the number


import math
import time

# refrenced from: https://www.geeksforgeeks.org/find-largest-prime-factor-number/)
def simple_primefact(n):
    maxPrime = -1
    # remove the even factors
    while (n%2==0):
        maxPrime = 2
        n = n >> 2
    #loop around the odd factors and remove each multiples of that number
    for i in (range(2,(int)(math.sqrt(n))+1)[1::2]):
        while (n%i==0):
            maxPrime = i
            n = n /i
    #return the max prime number
    #return the remainder or the maxPrime
    return n if n > 2 else maxPrime

#returns a list of prime factors of a number
#time complexity depends on the size of the number
#reference: https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
def FermatFactor(n,fact_list):
    # remove the even factors
    while (n%2==0):
        maxPrime = 2
        n = n >> 2
    a = math.ceil(math.sqrt(n))
    b2 = a*a - n
    while not isPerfectSquare(b2):
        a = a + 1
        b2 = a*a - n
    if a - math.sqrt(b2) == 1.0:
        fact_list.append(a + math.sqrt(b2))
    else:
        FermatFactor(a + math.sqrt(b2),fact_list)
        FermatFactor(a - math.sqrt(b2),fact_list)

#returns true if a number is a perfect square
#https://www.geeksforgeeks.org/check-if-given-number-is-perfect-square-in-cpp/
def isPerfectSquare(n):
  sr = math.sqrt(n); 
  return ((sr - math.floor(sr)) == 0);

def main():

    #simple method
    start_time = time.time()
    print(simple_primefact(600851475143))
    print("simple method --- %s seconds ---" % (time.time() - start_time))

    #fermat method
    start_time = time.time()
    lst = []
    FermatFactor(600851475143,lst)
    print(max(lst))
    print("fermat method --- %s seconds ---" % (time.time() - start_time))

    
if __name__=="__main__": 
    main()
