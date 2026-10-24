from collections import deque #para crear una cola

grafo = { 
    "A":["B","C"], #A te lleva hacia B o C
    "B":["D"], #B te lleva hacia D
    "C":["D"], #C te lleva hacia D
    "D":[] 
}

def bfs(inicio, meta):
    cola = deque([[inicio]])
    visitados = set() #visitados es un conjunto donde se anota lo explorado
    
    while cola:
        camino = cola.popleft() #saca la primera ruta de la cola
        nodo = camino[-1] #toma el último punto de la cola
        
        if nodo == meta:
            return camino #si el punto actual es la meta, se termina todo
        
        if nodo not in visitados:
            visitados.add(nodo) #si no se exploró ese punto, lo marca como visitado
            
            #Por cada vecino, hace una copia de la ruta actual
            #Agrega ese vecino
            #Pone la nueva ruta al final de la cola
            for vecino in grafo[nodo]:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
                
ruta = bfs("A", "D")
print("Ruta encontrada:", ruta)