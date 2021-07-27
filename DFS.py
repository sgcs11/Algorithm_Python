#Cyclic detection(순환 검출)
# back edge(역방향 간선)이 존재하면 cycle이 존재한다. (역도 성립)
V = [chr(ord("a")+i) for i in range(6)]
Adj = {"a":["b","d"],"b":["e"],"c":["e","f"],"d":["b"],"e":["d"],"f":["f"]}

parent={}
stack = {} #방문중인 노드 stack에 넣고 stack 있는 노드로 향하는 간선은 back edge로 간주
def DFS_visit(V,Adj,s):
    stack[s]=1#start
    for v in Adj[s]:
        if v not in parent:
            parent[v]=s
            DFS_visit(V,Adj,v)
        elif v in stack: #O(1)
            print(f"cycle detected : back end edge from {s} to {v}")
    del stack[s]#finish

def DFS(V,Adj):
    for s in V:
        if s not in parent:
            parent[s]=None
            DFS_visit(V,Adj,s)

DFS(V,Adj) #(V+E)

#toplogical sort(위상 정렬)
V = [chr(ord("A")+i) for i in range(9)]
Adj = {
    "G":["H"],
    "A":["B","H"],
    "B":["C"],
    "C":["F"],
    "D":["C","E"],
    "E":["F"],
    "F":[],
    "H":[],
    "I":[]
}
parent={}
order=[] #dfs순서대로 담음
def DFS_visit(V,Adj,s):
    for v in Adj[s]:
        if v not in parent:
            parent[v]=s
            DFS_visit(V,Adj,v)
    if s in order:
        order.remove(s)
    order.append(s)

def DFS(V,Adj):
    for s in V:
        if s not in parent:
            parent[s]=None
            DFS_visit(V,Adj,s)

DFS(V,Adj)
order.reverse()
print(order)