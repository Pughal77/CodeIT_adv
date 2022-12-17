
from time import time
from exchangeRates import exchangeRates
from sys import argv
import math

INF = 10000.0


def arbitrage(exchangeRates):

    # CONVERT EXCHANGE RATES TO LOG GRAPH
    logGraph = convertToLogGraph(exchangeRates)

    # RETRIEVES SHORTEST PATH TREE / NONE THROUGH BELLMAN FORD ALGO
    edge, edgeTo = bellmanFord(logGraph)
    # print(edge,edgeTo)
    # RETRIEVES EDGES INVOLVED IN CYCLE IF THERE IS ONE
    return searchForCycle(edge, edgeTo)


'''
convertToLogGraph:
    - This function takes in a graph of exchange rates, and returns an adjacency list with the same edges, but with every weight having the negative log10 function applied
'''


def convertToLogGraph(exchangeRates):
    new_exchange_rate = {}
    for vertex in exchangeRates.keys():
        index = 0
        new_exchange_rate[vertex] = []
        for edges in exchangeRates[vertex]:
            new_exchange_rate[vertex].append(
                (edges[0], edges[1], -math.log(edges[2], 10)))
            index += 1
    return new_exchange_rate


'''
bellmanFord:
    - This function will take in the logGraph (output of convertToLogGraph function), and returns the shortest path tree
    - The shortest path tree is essentially an adjacent list made up of the edges involved in the edgeTo list.
'''


def bellmanFord(logGraph):
    vertex_list = list(logGraph.keys())
    edgelist = []
    distTo = {}
    #last edge of shortp stored in dest
    edgeTo = {}
    for vertex in vertex_list:
        distTo[vertex] = INF
        edgelist.extend(logGraph[vertex])
        edgeTo[vertex] = [None] * 3
    #setting start to be 0
    distTo[vertex_list[0]] = 0
    count = 0
    while count <= len(logGraph)-1:
      for edge in edgelist:
          #to prevent uturn
          if edge[0] == edgeTo[edge[1]][1] and edge[1] == edgeTo[edge[1]][0]:
              continue
          #edge[0] = src,edge[1]=dest,edge[2] = weight
          if distTo[edge[1]] > distTo[edge[0]] + edge[2]:
              distTo[edge[1]] = distTo[edge[0]] + edge[2]
              edgeTo[edge[1]] = edge
              # print(count)
              if count == len(logGraph) - 1:
                #if edges are still being relaxed run search for cycle algo
                #edge[1] is the vertex that is start/end of -ve cycle
                # print(edge[1])
                #remove edgeTo[edge[1]] to prevent inf loop
                return edge[0], edgeTo
      count +=1
    return None, edgeTo


'''
searchForCycle:
    - This function takes in the shortest path tree (output of bellmanFord), and returns a list containing edges (excluding the weights) involved in the negative cycle.
    - For instance, for exchange rates 1, it should return: [('SGD', 'GBP'), ('GBP', 'USD'), ('USD', 'SGD')]

'''


def searchForCycle(edge, edgeTo):
    ive_cycle = []
    if edge != None:
        parent = edge
        while parent:
            path = [edgeTo[parent][0], edgeTo[parent][1]]
            ive_cycle.append(path)
            parent = edgeTo[parent][0]
            if parent == edge:
                return ive_cycle
    if edge == None:
        return []


def main():
    try:
        n = int(argv[1]) - 1
    except:
        print("No CLA inputted, defaulting to exchangeRate 1")
        n = 0

    start = time()
    print("Arbitrage: {}".format(arbitrage(exchangeRates[n])))
    end = time()
    print("Time taken for arbitrage function: {}s".format(end - start))


if __name__ == "__main__":
    main()
