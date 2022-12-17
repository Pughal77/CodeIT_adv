'''
    Problem #2: Implement the topological sort algorithm 
    - You are to implement the topological sort algorithm
    - Each function comes with instructions on how to implement them. 
    (Don't change anything that is already written for you)


    - The DirectedEdge class has been implemented for you and contains the following attributes:
        -> src: edge from
        -> dest: edge to

    - The Digraph class has been implemented for you and comes with the following:
        -> adjList: 2D list representing adj list of undirected graph.
        Each vertex points to a list of it's adjacent DirectedEdges

        -> addEdge: Takes in an edge as a tuple (src, dest) and adds it as a DirectedEdge to the adjList
        -> printGraph: prints the adj list of each vertex out

    - To test your implementation, run `python utils/topsort_test.py`
'''

from utils.helpers import Digraph
class cycle_detected_error(Exception):
  pass
def dfsRecurse(v, digraph, visited, revTO,visited_in_rec):
    list_of_dest = [x.dest for x in digraph.adjList[v]]
    for dest in list_of_dest:
      if dest in visited_in_rec:
        raise cycle_detected_error
    visited_in_rec.append(v)
    if visited[v]:
      return
    visited[v] = True
    for dest in digraph.adjList[v]:
        if not visited[dest.dest]:
            dfsRecurse(dest.dest, digraph, visited, revTO,visited_in_rec)
    revTO.append(v)
    

def topsort(digraph):
    """Topological sort algorithm

    Arguments
    ----------
    digraph: type `Digraph`
        -> Adjacency list undirected graph to sort
        -> Each vertex in adjList points to a list of DirectedEdges

    Return: 
    - None if digraph contains a cycle
    - A list of vertices where the vertices are sorted in topological order (starting from start) from left to right
    """
    # PSEUDO CODE
    # 1. Initialise visited array
    # 2. For each vertex not already visted, recursively visit all adjacent vertices if not already visited
    #    2a. Each time a vertex is visited, set visited[vertex] to True
    #    2b. Keep track of vertices currently on the recursive stack. If a vertex visited is on the 
    #        recursive stack, a cycle is present
    # 3. Return ordering of vertices visited in dfs reversed
    adjlist = digraph.adjList
    visited = [False] * len(adjlist)
    revTO = []
    for i in range(len(adjlist)):
      try:
        visited_in_rec = []
        dfsRecurse(i,digraph,visited,revTO,visited_in_rec)
      except cycle_detected_error:
        return None
    return revTO[::-1]
    

