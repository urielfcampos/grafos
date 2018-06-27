import numpy as np
import operator
import timing
import bell
import dijk
import floy
import kruskaltry
import art
import euler
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
    type_repr = ""
    adjMatrix = {}
    adjList = {}
    counter:int
    color = {"white": [], "gray": [], "black": []}
    pred = {}
    time = {}
    pai = dict()
    rank =dict()
    def file_treatment(self):
        with open("grafo.txt", "r") as file:
            for i, l in enumerate(file):
                pass
            input_test = ""
            node_names = []
            node_values = []
            file.seek(0)
            type = file.readline()
            self.type_repr = type.strip("\n")
            for x in range(i):
                input_test = file.readline()
                #print(input_test)
                intermediateSeperator = input_test.find("[")
                secondIntermediateSeperator = input_test.find("]")
                node_names.append(input_test[0:input_test.find(":")])
                intermediateString = input_test[intermediateSeperator + 1:secondIntermediateSeperator]
                intermediateString = intermediateString.replace(',' , ' ')
                node_values.append(intermediateString.split())
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

    def find_adj(self,edge:str,type_rep:int,grafo):
        names = []
        if type_rep ==0:
            for x in range(len(grafo[edge])):
                if grafo[edge][x]== "1":
                    names.append(self.find_name(x))
            return names
        if type_rep ==4:
            for x in range(len(grafo[edge])):
                if grafo[edge][x]== "1":
                    names.append(int(self.find_name(x)))
            return names
        if type_rep==1:
            return self.adjList[edge]
        if type_rep ==2:
            for x in range(len(grafo[edge])):
                if int(grafo[edge][x])>= int("1"):
                    names.append((int(grafo[edge][x]),edge,self.find_name(x)))
            return names
        if type_rep == 3:
            for x in range(len(grafo[edge])):
                if int(grafo[edge][x])>= int("1"):
                    names.append((self.find_name(x),int(grafo[edge][x])))
            return names

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

    def DepthFirstSearch(self,source,grafo,function_value):
        global counter_timer
        counter_timer =0
        global connected
        connected = []
        def visitDFS(node):
            global counter_timer
            global  connected
            counter_timer += 1
            connected.append(node)
            color["white"].remove(node)
            color["gray"].append(node)
            time[node] =counter_timer
            adjs = self.find_adj(node,0,grafo)
            for x in adjs:
                if x in color["white"]:
                    pred[x] = node
                    visitDFS(x)
            color["gray"].remove(node)
            color["black"].append(node)
            counter_timer +=1
            time_final[node]+= counter_timer

        def iterate_paths(vertex):
            path =[]
            if pred[vertex][0] != None:
                path.append(pred[vertex][0])
                path = path+iterate_paths(pred[vertex][0])
                print(path)
                return path
            else:
                return path
        color ={"white":[],"gray":[],"black":[]}
        pred = {}
        time ={}
        time_final = {}
        print("Comecando busca em profundidade")
        for x in grafo:
            color["white"].append(x)
            pred.update({x:[None]})
            time.update({x:counter_timer})
            time_final.update({x:counter_timer})
        if (function_value == "3"):
            for x in grafo:
                if x in color["white"]:
                    visitDFS(x)
        elif(function_value == "0"):
           while source:
            i = source.pop(0)
            if i not in color["black"]:
                visitDFS(i)
                connected.append("")


        #print(time_final)
        #print(time)
        #print(color["black"])
        finalizado = {}
        #print(pred)
        print("ordem de visita")
        for x in grafo:
            finalizado.update({x:time[x]})

        sorted_visita = sorted(finalizado.items(),key=operator.itemgetter(1))
        for x in sorted_visita:
            print("Vertice:"+list(x)[0])

        if (function_value == "5"):
            paths =[]
            valuesToTest =[]
            CaminhosFinais =[]
            #print(pred)
            for y in pred:
                for x in pred:
                    if y == pred[x][0]:
                        valuesToTest.append(y)

            for x in pred:
                if x not in valuesToTest:
                    CaminhosFinais.append(x)

            for x in CaminhosFinais:
                paths.append(list(x)+iterate_paths(x))
            return paths
        elif (function_value =="3"):
            return time_final
        else:
            return connected

    def FindConnectivity(self):
        transposed=self.adjMatrix.copy()
        matriz = []
        for x in transposed:
            matriz.append(transposed[x])
        transposedmatriz = np.transpose(matriz)
        transposedmatriz = transposedmatriz.tolist()
        print(list(transposedmatriz))
        for x,y in zip(transposed,transposedmatriz):
            transposed[x] = y[:]

        final1 = self.DepthFirstSearch("0",self.adjMatrix,"3").copy()
        stacked=[]
        for x in final1:
            stacked.append(final1[x])
        #print(stacked)
        stacked = sorted(stacked,reverse=True)
        #print(stacked)
        final2 = final1.copy()
        order_dfs = []
        for y in stacked:
            for x in final2:
                if y == final2[x]:
                    order_dfs.append(x)
        SCC = []
        SCC = self.DepthFirstSearch(order_dfs,transposed,"0")
        print("Componentes fortemente conexos :")
        formatado = ""
        for x in SCC :
            if x== "":
                formatado+= "/"
            else:
                formatado += x+"-"
        formatado = formatado[0:-1]
        for x in formatado.split("/"):
            print("Vertices:",x[0:-1])

    def make_set(self,v):
        self.pai[v] = v
        self.rank[v] = 0

    def find(self,v):
        if self.pai[v] != v:
           self.pai[v] = self.find(self.pai[v])
        return self.pai[v]

    def union(self,v1, v2):
        raiz1 = self.find(v1)
        raiz2 = self.find(v2)
        if raiz1 != raiz2:
            if self.rank[raiz1] > self.rank[raiz2]:
                self.pai[raiz2] = raiz1
            else:
                self.pai[raiz1] = raiz2
            if self.rank[raiz1] == self.rank[raiz2]:
                self.rank[raiz2] += 1

    def kruskal(self,graph):
        A = []
        B =[]
        for v in graph:
            self.make_set(v)
            AGM = set()
        for v in graph:
            A.append(self.find_adj(v, 2, graph))
        for i in A:
            for y in i:
                B.append(y)

        B.sort()
        for i in B:
            peso, v1, v2 = i
            if self.find(v1) != self.find(v2):
                self.union(v1, v2)
                AGM.add(i)
        return sorted(AGM)

    def add_edge(self, node1, node2, type):
        if type == 1:
            if self.adjMatrix[node1][self.find_value(node2)] == "1":
                print("Aresta ja existe")
            else:
                self.adjMatrix[node1][self.find_value(node2)] = "1"
                self.adjMatrix[node2][self.find_value(node1)] = "1"
        elif type == 0:
            self.adjMatrix[node1][self.find_value(node2)] = "1"
        elif type == 2:
            self.adjMatrix[node1][self.find_value(node2)] = input("Peso : ")

    def convert_to_djk(self,type):
        grafo = self.adjMatrix.copy()
        grafo_convertido = {}
        names = []
        if type ==0:
            for x in grafo:
                names.append(self.find_adj(x,3,grafo))
                for y in names:
                    if y == []:
                        grafo_convertido.update({x: None})
                    else:
                        grafo_convertido.update({x: y})
            self.adjList = grafo_convertido.copy()
        elif type ==1:
            for x in grafo:
                names.append(self.find_adj(x,4,grafo))
                for y in names:
                    if y == []:
                        grafo_convertido.update({x: None})
                    else:
                        grafo_convertido.update({x: y})
            self.adjList = grafo_convertido.copy()
        elif type == 2:
            for x in grafo:
                names.append(self.find_adj(x, 0, grafo))
                for y in names:
                    if y == []:
                        grafo_convertido.update({x: None})
                    else:
                        grafo_convertido.update({x: y})
            self.adjList = grafo_convertido.copy()
            print(self.adjList)


    def dij(self,fonte):
        print("Dijkstra:\n")
        distancias, antecedencias, existeCicloNeg = dijk.dijkstra(self.adjList, fonte)
        if existeCicloNeg:
            print("Existe pelo menos uma aresta com peso negativo, não se pode usar Dijkstra.")
        else:
            print("Distância da fonte", fonte, "para os nós:\t", distancias)
            print("Antecessores dos nós:\t\t\t", antecedencias)

    def bel(self):
        print("Bellman Ford:\n")
        distancias, antecedencias, cicloneg = bell.bellman_ford(self.adjList, "A")
        if cicloneg:
            print("Ciclo negativo encontrado.")
        else:
            print("Distância da fonte", "A", "para os nós:\t", distancias)
            print("Antecessores dos nós:\t\t\t", antecedencias)
    def flo(self):
        print("Floyd Warshall:\n")
        print("Grafo entrada:\n")
        grafo_flo=[]
        grafo_matriz =[]
        contadores = []
        counter = 0
        floDict = {}
        floDict2way ={}
        for x in self.adjMatrix:
            grafo_flo.append(x)
            grafo_matriz.append((self.adjMatrix[x]))
            contadores.append(counter)
            counter += 1
        for x, i in zip(contadores, grafo_flo):
            floDict.update({x: i})
            floDict2way.update({i:x})
        for x in range(len(grafo_matriz)):
            for y in range(len(grafo_matriz[x])):
                grafo_matriz[x][y] = int(grafo_matriz[x][y])
        for i in range(len(grafo_matriz)):
            print(grafo_matriz[i])
        grafo, antec = floy.floyd_warshall(grafo_matriz)
        print("\nDistâncias:\n")
        for i in range(len(grafo_matriz)):
            print(grafo_flo[i],grafo[i])
        print("\nAntecedências:\n")
        for i in range(len(grafo_matriz)):
            print(antec[i])
        x = floDict2way[input("Para caminhar no grafo informe o nó de partida:")]
        y = floDict2way[input("Informe o nó de chegada:")]
        floy.showPathFloy(antec, x, y,floDict)

    def find_cicle(self, source, grafo, function_value):
            nova = []
            ender = []
            is_here = []
            global counter_timer
            counter_timer = 0
            global connected
            connected = []

            def visitDFS(node):
                tired = []
                global counter_timer
                global connected
                counter_timer += 1
                connected.append(node)
                print("Visitando", node)
                color["white"].remove(node)
                color["gray"].append(node)
                time[node] = counter_timer
                print("Cores: ", color)
                adjs = self.find_adj(node, 0, grafo)
                print("Vizinhos: ", adjs)
                for x in adjs:
                    if x in color["white"]:
                        pred[x] = node
                        visitDFS(x)
                        print(x)
                    else:
                        nova.append(x)
                color["gray"].remove(node)
                color["black"].append(node)
                counter_timer += 1
                time_final[node] += counter_timer
                if not nova:
                    test = None
                else:
                    test = nova[0]

                for i in color["black"]:
                    if i not in tired and i != test and test is not None:
                        if i not in ender:
                            tired.append(i)


                if test in color["black"]:

                    tired.append(nova.pop())
                    ui = []
                    while tired:
                        ui.append(tired.pop())
                        for c in ui:
                            if c not in is_here:
                                is_here.append(c)
                if is_here and test in color["black"]:
                    is_here.append(test)
                elif len(nova) > 1 and len(ender) > 0:

                    nova.append(node)
                    nova.pop(0)
                    print(nova)
                for i in range(len(is_here)):
                    if is_here[0] not in ender:
                        ender.append(is_here[0])
                        is_here.pop(0)
                    elif is_here[0] in ender:

                        if ender.count(test) == 1:
                            ender.append(test)
                            ender.append("")
                            is_here.pop(0)
                    else:
                        is_here.pop(0)
                print("Finalizando", node)
                print("Cores finais: ", color)
                print("Ciclo final: ", ender)

            def iterate_paths(vertex):
                path = []
                if pred[vertex][0] != None:
                    path.append(pred[vertex][0])
                    path = path + iterate_paths(pred[vertex][0])
                    print(path)
                    return path
                else:
                    return path

            color = {"white": [], "gray": [], "black": []}
            pred = {}
            time = {}
            time_final = {}
            print("Comecando busca em profundidade")
            for x in grafo:
                color["white"].append(x)
                pred.update({x: [None]})
                time.update({x: counter_timer})
                time_final.update({x: counter_timer})
            if (function_value == "3"):
                for x in grafo:
                    if x in color["white"]:
                        visitDFS(x)
                    print("Sem suporte")
                    break
                print("Ainda sem suporte")

            return ender

    def bfs(self,graph, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)





def main_menu(grafo):
    x = True
    while(x):
        print("Imprimir grafo: 1")
        print("Adicionar Aresta: 2")
        print("Adicionar vertice: 3")
        print("Achar Componentes Conexos:4")
        print("Rodar Busca em Profundidade:5")
        print("Rodar Kruskal:6")
        print("Rodar Prim:7")
        print("Rodar Dijkstra:8")
        print("Rodar Bellmon-ford:9")
        print("Rodar Floyd Warshal:10")
        print("Achar pontos de articulacao:11")
        print("Achar ciclos:12")
        print("Ciclo de Euler:13")
        print("Menor Caminho :14")
        x = input()
        x = int(x)
        if x == 1:
            if grafo.type_repr == "0":
                print(grafo.adjMatrix)
                print("===================================")
            elif grafo.type_repr =="1":
                print(grafo.adjList)
                print("===================================")
        elif x == 2:
            grafo.add_edge(input("Vertice1"),input("Vertice 2"),input("Direcionado ?(0:para Nao direcionado, 1:Para direcionado sem peso, 2:para direcionado com peso"))
            print("===================================")
        elif x == 3:
            grafo.addNode(input("Tipo : 1 para lista de adj e 0 para matriz"))
            print("===================================")
        elif x == 4:
            grafo.FindConnectivity()
            print("===================================")
        elif x == 5:
            grafo.DepthFirstSearch(input("fonte"),grafo.adjMatrix,"3")
            print("===================================")
        elif x == 6:
            print(g.kruskal(g.adjMatrix))
            print("===================================")
        elif x == 7:
            kruskaltry.PRIM(g.adjMatrix)
            print("===================================")
        elif x == 8:
            grafo.convert_to_djk(0)
            grafo.dij(input("Informe a fonte"))
            print("===================================")
        elif x == 9:
            grafo.bel()
            print("===================================")
        elif x == 10:
            grafo.flo()
            print("===================================")
        elif x == 11:
            grafo.convert_to_djk(2)
            #print(grafo.adjList)
            print(art.art_poin(grafo.adjList))
            print("===================================")
        elif x == 12:
            g.find_cicle(input("fonte"), g.adjMatrix, "3")
            print("===================================")
        elif x == 13:
            g.convert_to_djk(1)
            euler.runEuler(g.adjList.copy())
            print("===================================")
        elif x ==14:
            g.convert_to_djk(2)
            print(g.bfs(g.adjList, input("Comeco"), input("Final")))
            print("===================================")


if __name__ == '__main__':
    g = grafos()
    g.file_treatment()
    main_menu(g)
    #g.convert_to_djk(2)
    #print(g.bfs(g.adjList,"0","5"))
    #euler.runEuler(g.adjList.copy())
    #main_menu(g)
    #g.convert_to_djk()
    #g.bel()
    #g.dij()
    #kruskaltry.PRIM(g.adjMatrix)
    #g.flo()
    #for x in g.adjList:
       #print("Adjaçentes de "+x,g.find_adj(x,1,g.adjList))
    #print(len(g.adjMatrix["0"]))
    #print(len(g.adjMatrix["8"]))
    #g.find_adj("4",0)
    #g.addNode(0)
    #g.DepthFirstSearch("0",g.adjMatrix,"3")
    #g.FindConnectivity()
    #print(g.kruskal(g.adjMatrix))