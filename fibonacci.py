"""выводит первые n членов последовательсти Фибоначчи"""
n = int(input())
f1, f2 = 0, 1
print("1", end=" ")
for i in range(n - 1):
    f1, f2 = f2, f1 + f2
    print(f2, end=" ")

# или
n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
