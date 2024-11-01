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

if __name__ == '__main__':
    func()
    printing()