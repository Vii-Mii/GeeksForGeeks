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

if __name__ == '__main__':
    func()
    printing()