
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
# https://www.csdojo.io/dpcode

# A naive recursive solution
def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

############### TOP DOWN APPROACH ##################

# A memoized solution OR Top-Down Approach
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result # Update solutions to sub-problems in end, which can be used later to check. If solution to subproblem is already present then just reuse it.
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)

############### BOTTOM-UP APPROACH ##################

# A bottom-up solution
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1) # Initialise an empty array of size n+1
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

#################### DRIVER CODE #####################

result1 = fib(5)
result2 = fib_memo(6)
result3 = fib_bottom_up(7)
print "Results are : %d %d %d" %(result1, result2, result3)
