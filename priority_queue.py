import heapq
a = [4,6,32,1,34,4,35443,1]
b = []
heapq.heapify(a) #O(N)

while a:#O(N)
    b.append(heapq.heappop(a)) #O(logN)

print(b)

#O(NlogN)