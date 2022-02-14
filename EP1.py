
import sys

class Cidade:

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.visitados = [0]*(self.N+1)
        self.bandeira = 0
        self.Cidade =[[0]*(self.N+1) for i in range(self.N+1)]
        self.pilha = [0]*(self.N+1)
        self.tam_pilha = 0
        

    def adiciona_aresta(self, V, W, P):
        if P == 1:
            self.Cidade[V][W] = 1                 
        else:
            self.Cidade[V][W] = self.Cidade[W][V] = 1    

    def conexo(self):
        for i in range(1,self.M):
            self.dfs(i,self.M)
            for v in range(0,self.M):
                if self.visitados[v] == -1:
                    self.bandeira = 0
                    break
            if self.bandeira == 0:
                break
        if self.bandeira == 1:
            return 1
        else:
            return 0

    def mostra_cidade(self):
        print('A cidade é:')
        for i in range(self.N):
            print(self.Cidade[i])

    def dfs(self,v,e):
        print('dfs')
        i = 0
        self.visitados[v] = 1
        for i in range(e):
            if self.Cidade[v][i] == 1 and self.visitados[i] == -1:
                self.dfs(i,e)
    

#linhas = sys.stdin.read().strip().split('\n')
linhas = '''4 5
1 2 1
1 3 2
2 4 1
3 4 1
4 1 2
0 0
'''.strip().split('\n')

for i in range(0,len(linhas)):
    linha = linhas[i].split(' ')
    if linha == ['0','0']:
        C.bandeira = False
        C.mostra_cidade()
        print(C.conexo()) 
        break
    if len(linha) == 2:
        if i > 0:
            C.bandeira = False
            C.mostra_cidade()
            print(C.conexo()) 
        C = Cidade(int(linha[0]),int(linha[1]))
    else:
        C.adiciona_aresta(int(linha[0]),int(linha[1]),int(linha[2]))
        