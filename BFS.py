V = 8
Adj = {}
Adj["s"]=["a","x"]
Adj["a"]=["z","s"]
Adj["z"]=["a"]
Adj["x"]=["a","s","d","c"]
Adj["d"]=["x","c","f"]
Adj["c"]=["x","d","f","v"]
Adj["f"]=["d","c","v"]
Adj["v"]=["f","c"]

#레벨(단계)별로 구분하여 실행하는 BFS 구현
#parent는 경로를 출력해야할 경우 부모를 찾아가면서 출력하기 위함
def BFS(V,Adj,s):
    level = {s:0}
    parent = {s:None}
    i = 1
    frontier = [s]
    while frontier:
        next = []
        for u in frontier:
            for v in Adj[u]:
                if v not in level:
                    level[v]=i
                    parent[v]=u
                    next.append(v)
        frontier = next
        i+=1
    print(level)
    print(parent)

BFS(V,Adj,"s")
