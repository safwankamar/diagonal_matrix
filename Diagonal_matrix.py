
#
n=int(input("enter the row"))
m=int(input("enter the column"))
def printPattern(n, m):
    arr = [[0 for i in range(n)]
           for j in range(m)]
    p = 1

    for k in range(n):
        i = k
        j = 0
        while (i >= 0):
            arr[i][j] = p
            p += 1
            j = j + 1
            i = i - 1

    for k in range(1, n, 1):
        j = k
        i = n - 1
        f = k
        while (i >= f):
            arr[i][j] = p
            p += 1
            j = j + 1
            i = i - 1

    for i in range(0, n, 1):
        for j in range(0, n, 1):
            print(arr[i][j], end=" ")

        print("\n", end="")



printPattern(n,m)