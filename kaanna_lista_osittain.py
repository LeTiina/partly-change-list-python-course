# tee ratkaisu tänne a[::-1]
def kaanna(lista: list, alku: int, loppu: int):
    lista1= []
    lista1 = lista[alku:loppu+1]
    lista2 = lista1[::-1]
    lista[alku:loppu+1] = lista2
    print(lista)

kaanna([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 0, 4)