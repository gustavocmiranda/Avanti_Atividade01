def func(lista1, lista2):
    final = []
    lista = set(lista1 + lista2) # soh pra diminuir um pouco o numero de iteracoes
    for e in lista:
        if e not in lista1 or e not in lista2:
            final.append(e)
    return final



lista1 = [1,2,3,4,5,6,7]
lista2 = [6,7,8,9,4,1]
print(func(lista1, lista2))