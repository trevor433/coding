a = [1,2,3,5]
b = [0]*4
n = 4
j = 0
for i in range(n-1,-1,-1):
    b[i] = a[j]
    n -= 1
    j+=1
print(b)
