k=10
L = [[] for i in range(k)]
A = {"a":3,"b":5,"c":7,"d":5,"e":5,"f":3,"g":6}
for i in A.keys():
    L[A[i]].append(i)

output = []
for i in range(k):
    output.extend(L[i])

print(output)