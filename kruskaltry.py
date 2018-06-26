# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys  # Library for INT_MAX

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent,grafo_prim):
        print ("Edge \tWeight")
        for i in range(1,self.V):

            print (grafo_prim[parent[i]],"-",grafo_prim[i],"\t",self.graph[i][ parent[i] ])

    # A utility function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = 100000000000

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph represented using
    # adjacency matrix representation
    def primMST(self,grafo_prim):

        #Key values used to pick minimum weight edge in cut
        key = [100000000000] * self.V
        parent = [None] * self.V # Array to store constructed MST
        key[0] = 0   # Make key 0 so that this vertex is picked as first vertex
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if (self.graph[u][v] > 0 and mstSet[v] == False and
                   key[v] > self.graph[u][v]):
                        key[v] = self.graph[u][v]
                        parent[v] = u

        self.printMST(parent,grafo_prim)



def PRIM(grafo):
    grafo_prim = []
    grafo_matriz =[]
    contadores= []
    counter = 0
    primDict = {}
    for x in grafo:
        grafo_prim.append(x)
        grafo_matriz.append((grafo[x]))
        contadores.append(counter)
        counter +=1
    for x,i in zip(contadores,grafo_prim):
        primDict.update({x:i})
    print(primDict)
    g = Graph(len(grafo_matriz))
    print(g.V)
    g.graph = grafo_matriz[:]
    for x in range(len(g.graph)):
        for y in range(len(g.graph[x])):
            g.graph[x][y] = int(g.graph[x][y])

    print(g.graph)
    g.primMST(primDict)



# Contributed by Divyanshu Mehta