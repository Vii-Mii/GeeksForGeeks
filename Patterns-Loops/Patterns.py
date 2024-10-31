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

pattern9(3)
print()
pattern9(5)