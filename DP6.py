#Heitor Bianchi - 12058730
#Matheus Silvério - 10258921

#O script segue a seguinte lógica:

#o scrip define a quantidade competidores, o grid de largada e o de chegada,
#em seguide percorre esse grid e calcula o avanço de cada um.
#competidores cuja movimentação ja foi calculada são removidos dos grids
#com isso sempre é observada a movimentação do mais avançado do grid

import sys

linhas = sys.stdin.read().strip().split('\n')

for i in range(0,len(linhas),3):
    ultrapssagens = 0
    competidores = int(linhas[i])
    largada = linhas[i+1].strip().split(' ')
    chegada = linhas[i+2].strip().split(' ')
    posicao = 0

    for compeitdor in range(0, competidores):
        if posicao < largada.index(chegada[posicao]):
            ultrapssagens += (largada.index(chegada[posicao])-posicao)
            largada.pop(largada.index(chegada[posicao]))
            chegada.pop(posicao)
            posicao = 0
        else:
            posicao+=1

    print(ultrapssagens)
    
