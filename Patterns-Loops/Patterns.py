from lib2to3.pytree import LeafPattern


def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

def pattern2(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

def pattern3(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

def pattern4(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print()

def pattern5(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print()

def pattern6(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end=" ")
        print()

def pattern7(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end=" ")

        for j in range(2*i+1):
            print("*",end=" ")

        for j in range(n-i-1):
            print(" ",end=" ")
        print()

def pattern8(n):
    for i in range(n):
        for j in range(i):
            print(" ", end=" ")

        for j in range(((2 * n) - (2 * i)) - 1):
            print("*", end=" ")

        for j in range(i):
            print(" ", end=" ")
        print()

def pattern9(n):
    pattern7(n)
    pattern8(n)

def pattern10(n):
    stars = 0
    for i in range(n*2):
        if i > n-1:
            stars -= 1
        for j in range(stars+1):
            print("*",end="")
        if i < n-1:
            stars += 1
        print()

def pattern11(n):
    for i in range(n):
        if i % 2 == 0:
            val = 1
        else:
            val = 0
        for j in range(i + 1):
            print(val, end=" ")
            val = 1 - val
        print()

def pattern12(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")

        for j in range((2 * n) - (2 * i)):
            print(" ", end=" ")

        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

def pattern13(n):
    val = 1
    for i in range(n):
        for j in range(i + 1):
            print(val, end=" ")
            val += 1
        print()

pattern13(3)
print()
pattern13(5)