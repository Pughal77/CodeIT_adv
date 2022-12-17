'''
    Problem #1: Implement depth-first search & breadth-first search
    - You are to implement the dfs & bfs functions below.
    - Each function comes with instructions on how to implement them. 
    (Don't change anything that is already written for you)

    - The Graph (Undirected) class has been implemented for you
    - It comes with the following attributes:
        -> adjList: 2D list representing adj list of undirected graph
    - It comes with the following methods:
        -> addEdge: Takes in an edge as a tuple (u, v) and adds an edge from u to v
        -> printGraph: prints the adj list of each vertex out

    - To test your implementation, run `python utils/traversal_test.py`
'''

from utils.helpers import Graph
from collections import deque

def dfsRecurse(v, graph, visited, result):
    visited[v] = True
    result.append(v)
    print(v)

    for dest in graph.adjList[v]:
        if not visited[dest]:
            dfsRecurse(dest, graph, visited, result)

def dfs(graph, start):
    
    #recursive version
    """Depth-first search from source

    Arguments
    ----------
    graph: type `Graph`
        -> Adjacency list undirected graph to traverse
    start: type `int`
        -> Vertex to begin depth-first search

    Return: 
    - A list of vertices where the vertices are visited in order, 
    by depth first search, from left to right
    """
    adjlist = graph.adjList
    visited = [False] * len(adjlist)
    result = []
    dfsRecurse(start,graph,visited,result)
    print(result)
    return result
    '''
    # PSEUDO CODE
    # 1. Initialise visited array
    # 2. From the starting vertex, recursively visit all adjacent vertices if not already visited
    #    2a. Each time a vertex is visited, set visited[vertex] to True
    # 3. Return ordering of vertices visited in dfs
    adjlist = graph.adjList
    visited = [False] * len(adjlist) 
    s = list([])
    visited[start] = True
    s.append(start)
    out = []
    while s:
      curr = s.pop()
      out.append(curr)
      print(curr)
      print(s)
      for n in adjlist[curr]:
        if visited[n]:
          continue
        s.append(n)
        visited[n] = True
        
    print(out)
    return out
    '''
    

def bfs(graph, start):
    """Breadth-first search from source

    Arguments
    ----------
    graph: type `Graph`
        -> Adjacency list undirected graph to traverse
    start: type `int`
        -> Vertex to begin breadth-first search

    Return: 
    - A list of vertices where the vertices are visited in order, 
    by breadth first search, from left to right
    """
    adjlist = graph.adjList
    visited = [False] * len(adjlist) 
    q = deque([])
    visited[start] = True
    q.append(start)
    out = []
    out.append(start)
    while q:
      curr = q.popleft()
      for n in adjlist[curr]:
        if visited[n]:
          continue
        q.append(n)
        visited[n] = True
        out.append(n)
    
    print(out)
    return out
        
    
    
    
    # PSEUDO CODE
    # 1. Initialise visited array
    # 2. Initialise empty queue
    # 3. Enqueue starting vertex & set visited[start] to True
    # 4. While queue is not empty:
    #    - Dequeue vertex and set visited[vertex] to True
    #    - Enqueue all adjacent vertices not already visited
    # 5. Return ordering of vertices visited in bfs


    return []