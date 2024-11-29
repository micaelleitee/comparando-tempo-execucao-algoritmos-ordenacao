def parent(i):
  return (i-1)//2
def left (i):
  return 2*i+1
def right (i):
  return 2*i+2

def max_heapify(lista, i):
  l = left(i)
  r = right(i)
  menor = i
  if l < (len(lista)) and lista[l] < lista[i]:
    menor = l
  else:
    menor = i
  if r < (len(lista)) and lista[r] < lista[menor]:
    menor = r
    
  if menor != i:
    lista[i], lista[menor] = lista[menor], lista[i]
    max_heapify(lista, menor)
  
def construir (lista):
  tamanho_lista = len(lista)
  for i in range ((tamanho_lista //2) -1, -1, -1):
    max_heapify(lista, i)

def heapsort(lista):
  construir(lista)
  tamanho_lista = (len(lista))
  for i in range (len(lista) -1, 0,-1):
    lista[0], lista[i] = lista[i], lista[0]
    tamanho_lista -= 1
    max_heapify(lista,0)
