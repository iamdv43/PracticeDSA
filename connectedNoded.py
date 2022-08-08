import collections
import math

def connectedSums(n, edges):
    n = 10
    nodes= [x for x in range(1,n+1)]
    edgeList=sorted(edges, key=lambda x:x[0])
    for x,y in edgeList:
        nodes[y-1]=nodes[x-1]
    connectednodes = {}
    for i in set(nodes):
        connectednodes[i] = nodes.count(i)
    res=0
    for i,c in connectednodes.items():
        res+=math.ceil(math.sqrt(c))
    return res

n = 10
edges = [[1, 2],[1, 3],[2,4],[3,5],[7,8]]
print("Connected Nodes: ", connectedSums(n, edges))