def mergesort (lista, inicio, fim):
  if  inicio < fim - 1:
    meio = (fim + inicio)//2
    mergesort(lista, inicio, meio)
    mergesort(lista, meio, fim)
    merge(lista, inicio, meio, fim)

def merge(lista,inicio, meio, fim):
  esquerda = lista[inicio:meio] + [float('inf')]
  direita = lista[meio:fim] + [float('inf')]
  topo_esquerda, topo_direita = 0, 0
  for i in range (inicio, fim):    
    if esquerda[topo_esquerda] < direita[topo_direita]:
      lista[i] = esquerda[topo_esquerda]
      topo_esquerda = topo_esquerda + 1
    else:
      lista[i] = direita[topo_direita]
      topo_direita = topo_direita + 1
