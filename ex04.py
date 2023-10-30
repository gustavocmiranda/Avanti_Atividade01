def func(lista):
    return sorted(lista, key= lambda x: x[0])




lista = [
    ('Carlos', 20),
    ('Alberto', 22),
    ('Eduardo', 23),
    ('Beto', 21),
]

print(func(lista))