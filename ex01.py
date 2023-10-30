
def primo(num):
    for i in range(2, num):
        if num%i == 0:
            return False
        
    if num == 0 or num == 1:
        return False
    return True


def func(numeros):
    primos = []
    for num in numeros:
        if primo(num):
            primos.append(num)
    return primos


lista = range(100)
print(func(lista))