
class node:
    name:str
    value:int
    matriz:list

    def __init__(self,name,value,matriz):
        self.name = name
        self.value = value
        self.matriz = matriz
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

    def file_treatment(self):
        with open("grafo.txt", "r") as file:
            for i, l in enumerate(file):
                pass
            input_test = ""
            node_names = []
            node_values = []
            file.seek(0)
            type = file.readline()
            for x in range(i-1):
                input_test = file.readline()
                print(input_test)
                intermediateSeperator = input_test.find("[")
                node_names.append(input_test[0])
                intermediateString = input_test[intermediateSeperator + 1:len(input_test) - 2]
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





if __name__ == '__main__':
    g = grafos()
    g.file_treatment()
    print(g.identify_edge(1,"0","1"))
    g.find_adj("4",1)

