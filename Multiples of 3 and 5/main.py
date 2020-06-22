# Shreyas Poyrekar
# 06/22/2020
# problem: Multiples of 3 and 5 (Project Euler)
# prints the sum of all the multiples of 3 or 5 below 1000

def sumofn(n):
    # returns sum of n numbers
    return n * (n + 1)/2

def main():
    # (sum of mutliples of 3) + (sum of mutliples of 5) - (sum of mutliples of 15)
    sum =  3 * sumofn(333) + 5 * sumofn(199) - 15 * sumofn(66)
    print(sum)
    

if __name__=="__main__": 
    main()
