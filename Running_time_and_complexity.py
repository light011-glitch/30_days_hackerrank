# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
from math import sqrt

T = int(input())


def isPrime(n):
    if n>1:
        for i in range(2, math.ceil(sqrt(n))+1):
            if n % i is 0:
                return False
        return True


for _ in range(T):
    n = int(input())

    if n == 2:
        print("Prime")
    elif n>2 and isPrime(n):
        print("Prime")
    else:
        print("Not prime")
