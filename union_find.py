import sys

R, C = map(int,sys.stdin.readline().split())
arr = [[0 for j in range(C)]for i in range(R)] #맵 배열
parents = [i for i in range(R*C)] #부모 배열
rank = [1 for i in range(R*C)] #랭크 배열

for i in range(R):
        arr[i]=list(sys.stdin.readline().rstrip('\n'))

def find(u):
    if u ==parents[u]: #자기 자신이 부모일 경우 자신이 리턴됨
        return u
    p = find(parents[u]) #아닐 경우 부모의 부모 재귀 탐색 결과는 최종 부모가 리턴됨
    parents[u]=p
    return parents[u]

def union(u,v):
    u = find(u) #u의 부모를 찾음
    v = find(v) #v의 부모를 찾음

    if u == v: #만약 부모가 같다면 union이 필요없어 리턴
        return        
    if rank[u] < rank[v]: #만약 v의 랭크가 크다면 u를 v에 붙여준다
        parents[u]=v
    else: #그외의 경우 v를 u에 붙여준다
        parents[v]=u
    if rank[u] == rank[v]: #u에 붙여줄때 u,v의 랭크가 같으면 u를증가
        rank[u]+=1