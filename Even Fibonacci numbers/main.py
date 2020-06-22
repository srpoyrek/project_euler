# Shreyas Poyrekar
# 06/22/2020
# problem: Even Fibonacci numbers (Project Euler)
# the sum of the even-valued terms in the Fibonacci sequence (starting with 1 and 2) whose values do not exceed four million

def is_even(n):
    # returns ture if the number is even
    return n % 2 == 0

def main():
    a = 1 #1st value
    b = 2 # 2nd value
    temp = 0 #swaping variable
    sum = 2 # b=2 is even add it to sum 
    while (a + b) < 4000000 :
        temp = b
        b = a + b
        a = temp
        if is_even(b):
            sum += b
    print(sum)
    

if __name__=="__main__": 
    main()
