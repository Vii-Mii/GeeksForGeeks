class Solution:
    def lcmAndGcd(self, A, B):
        val = A * B
        large = max(A, B)
        small = min(A, B)
        lcm = 0
        for i in range(large, A * B + 1, large):
            if i % small == 0:
                lcm = i
                break

        while (A > 0 and B > 0):
            if A > B:
                A = A % B
            else:
                B = B % A
        gcd = A if A else B
        return [lcm, gcd]

#Note (A * B) // gcd will be the LCM
