
class node:
    name:str
    value:int
    matriz:list

    def __init__(self,name,value,matriz):
        self.name = name
        self.value = value
        self.matriz = matriz
        if type(matriz)==str:
            self.matriz=matriz.split(' ')
    def __str__(self):
        return "(%s)"%(self.name)
    def __repr__(self):
        return "(%s)" % (self.name)
class grafos:

    nodes_list = []
    """"{"A": [0, 1, 0, 1, 1, 0, 0, 0],
     "B": [1, 0, 1, 0, 0, 1, 0, 0],
     "C": [0, 1, 0, 1, 0, 0, 0, 1],
     "D": [1, 0, 1, 0, 0, 0, 1, 0],
     "E": [1, 0, 0, 0, 0, 1, 1, 0],
     "F": [0, 1, 0, 0, 1, 0, 0, 1],
     "G": [0, 1, 0, 1, 1, 0, 0, 1],
     "H": [0, 0, 1, 0, 0, 1, 1, 0]} """
    adjMatrix = {}
    adjList = {}
    counter:int
    def file_treatment(self):
        with open("grafo.txt", "r") as file:
            for i, l in enumerate(file):
                pass
            input_test = ""
            node_names = []
            node_values = []
            file.seek(0)
            type = file.readline()
            for x in range(i):
                input_test = file.readline()
                print(input_test)
                intermediateSeperator = input_test.find("[")
                secondIntermediateSeperator = input_test.find("]")
                node_names.append(input_test[0])
                intermediateString = input_test[intermediateSeperator + 1:secondIntermediateSeperator]
                node_values.append(list(intermediateString))
            counter = 0
            for x in node_values:
                for y in x:
                    if y == ",":
                        counter += 1
            for x in range(counter):
                for y in node_values:
                    if "," in y:
                        y.remove(",")
            zipped = zip(node_names, node_values)
            nodes = []
            counter = 0
            for i in zipped:
                i = list(i)
                nodes.append(node(i[0], counter, i[1]))
                counter += 1
            self.nodes_list = nodes[:]
            self.create_repr(int(type))
            self.counter=counter
    def addNode(self,type):
        newNode = node(input("nome do vertice"),self.counter+1,input("adjacentes"))
        if type == 1:
            if newNode.name in self.adjList:
                print("Vertice ja existente")
                return 0
            else:
                for x in newNode.matriz:
                    if x not in self.adjList:
                        print("nao existe esse vertice",x)
                        return 0
                self.nodes_list.append(newNode)
                self.create_repr(type)
                self.updateAdjUndirected(newNode, type)
        elif type ==0:
            if newNode.name in self.adjMatrix:
                print("vertice ja existente")
                return 0
            else:
                for x in newNode.matriz:
                    if x not in self.adjMatrix:
                        print("Nao existe esse vertice",x)
                        return 0
                self.nodes_list.append(newNode)
                repr = ["0" for i in range(len(self.adjMatrix)+1)]
                self.adjMatrix.update({newNode.name:repr})
                self.updateAdjUndirected(newNode, type)

    def updateAdjUndirected(self,newNode,type):
        if type == 1:
            for x in newNode.matriz:
                for y in self.adjList:
                    if x == y:
                        updateValue = self.adjList[y]
                        updateValue.append(newNode.name)
                        self.adjList[y] = updateValue
            print(self.adjList)
        elif type ==0:
            for x in newNode.matriz:
                valueAdd = self.find_value(x)
                self.adjMatrix[newNode.name][valueAdd] = "1"
            print(self.adjMatrix)
            for y in self.adjMatrix:
               if y in newNode.matriz:
                   self.adjMatrix[y].append("1")
               else:
                   self.adjMatrix[y].append("0")


    def create_repr(self,type):
        repr_graph = {}
        if type ==0:
            for x in self.nodes_list:
                repr_graph.update({x.name:x.matriz})

            self.adjMatrix.update(repr_graph)
        elif type==1:
            for x in self.nodes_list:
                repr_graph.update({x.name: x.matriz})
            self.adjList.update(repr_graph)
            print(self.adjList)
    def find_value(self,edge1:str):
        value = 0
        for x in self.nodes_list:
            if x.name==edge1:
                value = x.value
                break
        return value
    def find_name(self,value:int):
        name:str
        for x in self.nodes_list:
            if x.value==value:
                name = x.name
                break
        return name
    def identify_edge(self,type_rep:int,edge:str,edge1:str):
        if type_rep == 0:
            value = self.find_value(edge1)
            if self.adjMatrix[edge][value] == "1":
                return True
            else:
                return False
        elif type_rep ==1:
            if edge1 in self.adjList[edge]:
                return True
            else:
                return False
    def find_adj(self,edge:str,type_rep:int):
        names = []
        if type_rep ==0:
            for x in range(len(self.adjMatrix[edge])):
                if self.adjMatrix[edge][x]== "1":
                    names.append(self.find_name(x))
            print(names)
        if type_rep==1:
            print(self.adjList[edge])
    def remove_node(self,type,node):
        if type == 0:
            self.adjMatrix.pop(node,None)
            for y in self.adjMatrix:
                self.adjMatrix[y].pop(self.find_value(node))
        elif type ==1:
            self.adjList.pop(node,None)
            for y in self.adjList:
                if node in self.adjList[y]:
                    self.adjList[y].remove(node)



if __name__ == '__main__':
    g = grafos()
    g.file_treatment()
    #print(g.identify_edge(0,"0","1"))
    #g.find_adj("4",0)
    #g.addNode(0)
    print(g.adjList)
    g.remove_node(1,"0")
    print(g.adjList)

