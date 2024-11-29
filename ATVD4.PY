import time
import matplotlib.pyplot as plt
from mergesort import mergesort
from heapsort import heapsort
import random


x = [100,200,300]
lista_m = []
lista_h = []
for i in range(len(x)):
  lista = []
  for j in range(x[i]):
    lista.append(random.randint(0,100))
  lista2 = lista.copy()
  lista3= lista.copy()
  inicio_merge = time.time()*1000
  mergesort(lista,0,(len(lista2)))
  fim_merge = time.time()*1000
  delta_merge = fim_merge-inicio_merge
  lista_m.append(delta_merge)
  inicio_heap = time.time()*1000
  heapsort(lista3)
  fim_heap = time.time()*1000
  delta_heap = fim_heap-inicio_heap
  lista_h.append(delta_heap)

plt.plot(x,lista_m)
plt.plot(x,lista_h)
plt.show()