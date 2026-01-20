"""немного теории перестановок"""

import time
import math


def swap(ls, a, b):
    A = ls[a]
    ls[a] = ls[b]
    ls[b] = A


def all_permutes_recursive(n, per=None):
    if per == None:
        per = list(range(n))
    if n == 1:
        print(per)
        return
    N = len(per)
    for i in range(n):
        swap(per, N - n, N - n + i)
        all_permutes_recursive(n - 1, per)
        swap(per, N - n, N - n + i)


def permute_mult(g, f):
    # return [f[gi] for gi in g]
    res = list(range(len(g)))
    for i in range(len(f)):
        res[i] = f[g[i]]
    return res


def permute_power(F, n):
    f = F
    res = list(range(len(f)))
    while n > 0:
        if n % 2 == 1:
            res = permute_mult(res, f)
        f = permute_mult(f, f)
        n //= 2  
    return res


start_time = time.time()

# all_permutes_recursive(4)

# g = [3, 0, 2, 1]
# f = [0, 2, 1, 3]
# print(permute_mult(g, f))
# print(permute_mult(f, g))

f = [0, 2, 1, 3]
n = 10
g = permute_power(f, n)

print(n)

print(f"Elapsed time: {time.time() - start_time:.4f} seconds")
