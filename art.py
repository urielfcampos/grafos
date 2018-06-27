
import copy
G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B'],
         'F': ['C'],
         'G': ['C']}


def art_poin(G):
    art = []
    for key in G:
        print(key)
    for key in G:
        print(G)
        v = copy.deepcopy(G)
        if key is int:
            z = int(key)
        else:
            z = key
        print("Deletar: ")
        print(z)
        del v[key]
        print("Novo Grafo")
        print(v)
        for k in v:
            if z in v[k]:
                v[k].remove(z)
        for k in v:
            i = comp_conex(v, k)
            print("Visitados")
            print(i)
            if len(i) < len(v):
                art.append(key)
            break
    if not art:
        return "Nao ha articulacoes"
    else:
        return 'Os pontos de articulacao sao: %s' % art


def comp_conex(graph, start):
    explored = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            print("Visitados : %s" % explored)
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored


#print(art_poin(graph))