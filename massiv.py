#1- misol
n, m = map(int,input().split())
mat = []
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(5*i)
    mat.append(arr)

for i in range(m):
    for j in range(n):
        print(mat[j][i],end=' ')
    print()