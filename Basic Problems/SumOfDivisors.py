class Solution:
    def sumOfDivisors(self, N):
        #code here
        def divisors(N):
            val = 0
            for i in range(1,int(N**0.5)+1):
                if N % i == 0:
                    val += i
                    if N//i != i:
                        val += N//i
            return val
        final = 0
        for i in range(1,N+1):
            final += divisors(i)
        return final

    #optimized approach
    def sumOofDivisors(self, n):
        res = 0
        for i in range(1, n + 1):
            res += i * (n // i)
        return res

