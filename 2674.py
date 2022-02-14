# Heitor Bianchi - 12058730
# Matheus Silvério - 10258921

# o script recebe a entrada com vários números e testa cada um deles a partir de duas funções booleanas criadas para categoriza-los como
# primo ou super primo. Caso nenhuma delas encontre o padrão esperado o número é definido como nada. Para cada número testado sua 
# categoria é printada como é esperado pelo exercício

from math import sqrt
import sys

# função binária que identifica os primos
def Primo(num):
    if (num == 2):
        return True
    if (num == 0 or num == 1 or (num % 2 == 0)):
        return False
    for i in range(3, int(sqrt(num)) + 2):
        if (num % i == 0):
            return False
    return True

# função que identifica os super primos
def Super(num):
    while num >= 10:
        s = num % 10
        num = int(num / 10)
        if not Primo(s):
            return False
    if(num == 2 or num == 3 or num == 5 or num == 7):
        return True
    else:
        return False

numeros = sys.stdin.read().strip().split('\n')

# laço que categoriza cada número como Super, Primo ou Nada
for numero in numeros:
    num = int(numero)
    if not Primo(num):
        print('Nada')
    else:
        if Super(num):
            print('Super')
        else:
            print('Primo')
