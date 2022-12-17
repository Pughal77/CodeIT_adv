from sys import argv
import csv
from collections import deque

'''
shortestPaths

    - This function takes in a user (vertex) and the adjacency list, and returns a dictionary for each shortest path that exists from that vertex to any other in the network. For instance, consider the following network:

    - For instance, for network5.csv, shortestPath("Ann", adjList) should return:
        {
        	"Eve": [ "Kim" ],
        	"Max": [ "Kim" ],
        	"Luke": [ "Kim", "Eve" ]
        }
    - This dictionary should not include keys who the start has a direct edge to (e.g. "Kim") and keys who the start has no path to. 
    - When there are multiple shortest paths, always choose the one that has lower alphabetical order
'''


  
def bfs (start,adjList):
  visited = {}
  for vert in adjList.keys():
    visited[vert] = False
  q = deque()
  q.append(start)
  visited[start]=True
  result = {}
  path_taken = {}
  for vert,adj_verts in adjList.items():
    adjList[vert] =sorted(adj_verts)
  while q:
    curr = q.popleft()
    
    if curr != start and curr not in adjList[start]:
      result[curr] = path_taken[curr]
    
    for nb in adjList[curr]:
      if visited[nb]:
        continue
      q.append(nb)
      visited[nb] = True
      path_taken.setdefault(nb,[])
      if curr != start:
        path_taken[nb].extend(path_taken[curr])
        path_taken[nb].append(curr)
  return result
      
def shortestPaths(start, adjList):
    # TO IMPLEMENT
    
  result = bfs(start,adjList)
  return result
'''
betweennessCentrality 

    - This function takes in the adjacency list and returns a dictionary where each vertex is a key and it's betweenness centrality is the value
    - It should make use of the shortestPaths function
    - For instance: betweennessCentrality(adjList) for the above network should return: {'Ann': 0, 'Kim': 3, 'Eve': 2, 'Max': 0, 'Luke': 0}
'''
def betweennessCentrality(adjList):
    # TO IMPLEMENT
  key_list = list(adjList.keys())
  bC_value = {}
  final_result = {}
  for vert in adjList.keys():
    bC_value[vert] = 0
    final_result[vert] = []
  
  for vert in adjList.keys():
    result = shortestPaths(vert,adjList)
    for key in result.keys():
      final_result[key].extend(result[key])
     
  for vert in final_result.keys():
    for node in final_result[vert]:
      bC_value[node] += 1
  return bC_value

'''
    - In main, we help you to read from the csv file, through a command line argument, and create the adjacency list for the edges. This is stored in a dictionary where each key is a vertex in the network and value is a list of edges for that vertex. 
    - To test, for instance, network5.csv, you may run `python centrality.py network5.csv`
'''
def main():

    if len(argv) < 2:
        print("Require network file to load edges")
        return

    adjList = {}
    with open("networks/" + argv[1], "r") as csv_file:
        myReader = csv.reader(csv_file)
        for row in myReader:
            u, v = row[0], row[1]
            if u not in adjList:
                adjList[u] = []
            if v not in adjList:
                adjList[v] = []
            adjList[u].append(v)

    print(betweennessCentrality(adjList))


if __name__ == "__main__":
    main()
