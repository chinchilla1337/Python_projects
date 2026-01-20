a = [3,5,6,7,2,1]

n = len(a)
for i in range(n-1):
    b = max(a[:n-1-i])
    a[a.index(b)]=a[-1-i]
    a[-1-i] = b

# реализация алгоритма сортировки выбором

print(a)
