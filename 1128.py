import sys

N = 10

ret = [0]*N
o = [0]*N
adjacentes = [[]]*N
cont = 0

def dfs(i):
    if ret[i] != -1:
        return ret[i]
    o[i] = cont + 1
    ret[i] = o[i]

    for j in range(0,len(adjacentes[i]),1):
        ret[i] = min(ret[i],dfs(adjacentes[i][j]))
    return ret[i]

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
    if len(linha) == 2:
        if i > 0:
            if i >=n:
                print('1\n')
            else:
                print('0\n')
        if linha == ['0','0']:
            break
        n = int(linha[0])
        m = int(linha[1])
        cont = 0
        for i in range(0,n,1):
            ret[i] = -1
            o[i] = -1
            adjacentes[i].clear()
    else:
        for i in range(0,m,1):
            v = int(linha[0])
            w = int(linha[1])
            p = int(linha[2])
            adjacentes[v-1].append(w-1)
            if p == 2:
                adjacentes[w-1].append(v-1)
        dfs(0)
        i = 1
        while i < n and o[i] > ret[i]:
            i+=1
            