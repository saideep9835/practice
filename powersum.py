# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def powerSum(n, k):
    # Your code goes here...
    b=0
    if n>0 and k>0:
        for i in range(1,n+1):
            b = b+i**k
        return b

    return 0

# Write your own test cases here...
print(powerSum(2,4))
print(powerSum(3,4))
print(powerSum(4,4))
print(powerSum(5,4))
print ("All test cases passed...")