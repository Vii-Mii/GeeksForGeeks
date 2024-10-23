class Solution:
    def isPrime (self, N):
        # code here
        if N == 1:
            return 0
        if N == 2:
            return 1
        for i in range(2,int(N**0.5)+1):
            if N % i == 0:
                return 0
        else:
            return 1

# You can also find the prime number by the logic of divisors