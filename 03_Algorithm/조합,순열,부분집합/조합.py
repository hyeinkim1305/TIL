
def f(i, j, n, r):
    if i == r:
        print(c)
    else:
        for k in range(j, n-r+i+1):
            c[i] = A[k]
            f(i+1, k+1, n, r)

n = 5
r = 3
A = [1, 2, 3, 4, 5]
c = [0] * r

f(0, 0, n, r)