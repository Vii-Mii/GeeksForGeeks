# Recursion : When a function call itself again and again
# Until a specific condition met (Base case or Base condition)

cnt = 0
def func():
    global cnt
    if cnt == 2:
        return
    print(cnt)
    cnt += 1
    func()

# Infinite Recursion
def printing():
    print("Calling function")
    printing()

def printGfg(self, n):
    # Code here
    if n == 0:
        return
    print("GFG", end=" ")
    self.printGfg(n - 1)

def printNos(self, n):
    # Your code here
    if n == 0:
        return
    self.printNos(n - 1)
    print(n, end=" ")

def printNos(self, n):
    # Code here
    if n == 0:
        return
    print(n, end=" ")
    self.printNos(n - 1)

# sum of N numbers using recursion
def summ(n):
    if n == 0:
        return 0
    return n + summ(n-1)

# factorial for N numbers using recursion]
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

# Reverse an array using recursion
def reverse(arr,n,i):
    if i >= n//2 :
        return
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
    reverse(arr,n,i+1)


# Palindrome using recursion
def palindrome(str,n,i):
    if i >= n//2:
        return True
    if str[i] != str[n-i-1]:
        return False
    return palindrome(str,n,i+1)

# Fibinocci
def fibinocci(n):
    if n <= 1:
        return n
    return fibinocci(n-1) + fibinocci(n-2)

if __name__ == '__main__':
    print(summ(6))
    print(fact(6))
    arr = [1,4,2,5,6,7]
    reverse(arr,6,0)
    print(arr)
    str = "racehar"
    print(palindrome(str,7,0))
    print(fibinocci(5))
