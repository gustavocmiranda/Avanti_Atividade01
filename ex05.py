def func(lista):
    maior = -99999999
    menor = 99999999
    for num in lista:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    return menor, maior


lista = range(1000)

print(func(lista))