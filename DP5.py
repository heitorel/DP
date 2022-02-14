import sys

#Heitor Bianchi - 12058730
#Matheus Silvério - 10258921

#O script segue a seguinte lógica:

#Para cada linha ele define um valor atingido de caracteres a serem economizados para cada palavra
#a partir de sua tamanho e sua frequencia na frase. Após isso identifica-se qual palavra para cada
#letra inicial possui o maior potencial econômico e então abrevia essa palavra para o padrão desejado
#em cada uma de suas aparições na linha. Ao final da execução é exibida a versão da linha abreviada,
#a quantidade de abreviações e a "legenda" das mesas!


def frequencia(lista, item): 
    freq = 0
    for i in lista: 
        if i == item: 
            freq = freq + 1
    return freq

#linhas = sys.stdin.read().strip().split('\n')
linhas = '''abcdef abc abc abc
abcd abc abc abc
abcd abcd abc abc abc
.'''.strip().split('\n')

for l in linhas:

    abreviadas = 0

    if l == '.':
        print('\n')
        continue
    
    abreviacoes = {'a':' ','b':' ','c':' ','d':' ','e':' ','f':' ','g':' ','h':' ','i':' ','j':' ',
            'k':' ','l':' ','m':' ','n':' ','o':' ','p':' ','q':' ','r':' ','s':' ','t':' ',
            'u':' ','v':' ','w':' ','x':' ','y':' ','z':' ',
           }

    abreviaveis={}

    lista_abreviaveis = l.split()

    for palavra in lista_abreviaveis:
        freq = frequencia(lista_abreviaveis,palavra)
        abreviaveis[palavra] = (len(palavra)-1)*freq
        if (len(abreviacoes[palavra[0]])-1)*frequencia(lista_abreviaveis,abreviacoes[palavra[0]]) <= (len(palavra)-2)*freq and len(palavra) > 2:
            abreviacoes[palavra[0]] = palavra
    
    linha = l
    linha_lista = linha.split()

    linha_oficial = linha.split()
    palavra = 0
    for palavra in range(len(linha_oficial)):
            if linha_oficial[palavra] == abreviacoes.get(linha_oficial[palavra][0]):
                linha_oficial[palavra] =  abreviacoes[linha_oficial[palavra][0]][0] + '.'
    
    print(' '.join(linha_oficial))

    for letra in abreviacoes:
        if abreviacoes[letra] != ' ':
            abreviadas = abreviadas + 1
    
    print(abreviadas)

    for letra in abreviacoes:
        if abreviacoes[letra] != ' ':
            print(abreviacoes[letra][0]+'. = '+abreviacoes[letra])

