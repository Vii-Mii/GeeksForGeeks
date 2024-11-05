

# return sorted(list(set(a) | set(b))
# Time complexity : O(n+m)log(n+m)
# space complexity : O(n+m)
def findUnion(a, b):
    temp = []
    i = 0
    j = 0
    while i <= len(a) - 1 and j <= len(b) - 1:
        if a[i] <= b[j]:
            if not temp or temp[-1] != a[i]:
                temp.append(a[i])
            i += 1
        else:
            if not temp or temp[-1] != b[j]:
                temp.append(b[j])
            j += 1

    while i <= len(a) - 1:
        if temp[-1] != a[i]:
            temp.append(a[i])
        i += 1
    while j <= len(b) - 1:
        if temp[-1] != b[j]:
            temp.append(b[j])
        j += 1

    return temp

# Time complexity : O(n+m)
# space complexity : O(n+m)