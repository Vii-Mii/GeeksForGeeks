class Solution:
    def evenlyDivides(self, N):
        cnt = 0
        temp = N
        while (N > 0):
            digit = N % 10
            if digit != 0 and temp % digit == 0:
                cnt += 1
            N //= 10

        return cnt