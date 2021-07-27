L = [15,271,1001,64,25,120,50,17,39,28]


# 자릿수 구하기
max=0
for i in L:
    if max<i:
        max = i

powed=1
# 정렬
for i in range(len(str(max))):
    Queue = [[]for i in range(10)]
    
    for j in L:
        temp = (j//powed)%10
        Queue[temp].append(j)
    L.clear()

    for j in Queue:
        L.extend(j)
    powed*=10
print(L)