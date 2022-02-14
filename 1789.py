import sys

nivel1 = 1
nivel2 = 2
nivel3 = 3

linhas = sys.stdin.read().strip().split('\n')

for i in range(0,len(linhas),2):
    lesmas = linhas[i].strip().split(' ')
    velocidades = linhas[i+1].strip().split(' ')
    nivel_atual = 0
    for j in range(0,len(velocidades)):
        velocidade = int(velocidades[j])
        if velocidade < 10 and nivel_atual < nivel1:
            nivel_atual = nivel1
        if velocidade >= 10 and velocidade < 20 and nivel_atual < nivel2:
            nivel_atual = nivel2
        if velocidade >= 20 and nivel_atual < nivel3:
            nivel_atual = nivel3
    print(nivel_atual)
print('\n')
