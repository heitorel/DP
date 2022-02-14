/*
 * Grupo 20
*/

/*
Numa certa cidade há N intersecções ligadas por ruas de mão única e ruas com mão dupla de direcão. 
É uma cidade moderna, de forma que muitas ruas atravessam túneis ou têm viadutos. 
Evidentemente é necessário que se possa viajar entre quaisquer duas intersecções, isto é, 
dadas duas intersecções V e W, deve ser possível viajar de V para W e de W para V.

Sua tarefa é escrever um programa que leia a descrição do sistema de tráfego de uma cidade e determine se o requisito de conexidade é satisfeito ou não.

Entrada
A entrada contém vários casos de teste. A primeira linha de um caso de teste contém dois números inteiros N e M, 
separados por um espaço em branco, indicando respectivamente o número de intersecções (2 ≤ N ≤ 2000) e o número de ruas (2 ≤ M ≤ N(N−1)/2). 
O caso de teste tem ainda mais M linhas, que contêm, cada uma, uma descrição de cada uma das M ruas. A descrição consiste de três inteiros V, W e P, 
separados por um espaço em branco, onde V e W são identificadores distintos de intersecções (1 ≤ V, W ≤ N , V ≠ W ) e P pode ser 1 ou 2; se P = 1 então a 
rua é de mão única, e vai de V para W; se P = 2 então a rua é de mão dupla, liga V e W. Não existe duas ruas ligando as mesmas intersecções.

O ultimo caso de teste é seguido por uma linha que contém apenas dois números zero separados por um espaço em branco.

Saída
Para cada caso de teste seu programa deve imprimir uma linha contendo um inteiro G, onde G é igual a 1 se o requisito de conexidade está satisfeito, ou G é igual a 0, caso contrário.


Exemplo de Entrada	Exemplo de Saída
4 5                 1
1 2 1
1 3 2
2 4 1
3 4 1
4 1 2
*/

#include <bits/stdc++.h>

using namespace std;

#define N 2000

// vetores de apoio
int vizinhos[N];
int auxiliar[N];
vector<int> adjacentes[N];

int contador;

// busca em profundiada 
// complexidade O(|V| + |A|)
int buscaprofunda (int i) {

    // Casos base
    if (vizinhos[i] != -1) 
        return vizinhos[i];

    auxiliar[i] = contador++;
    vizinhos[i] = auxiliar[i];

    for (int j = 0; j < adjacentes[i].size(); j++) {
        vizinhos[i] = min(vizinhos[i], buscaprofunda(adjacentes[i][j]));   
    }

    // Caso final
    return vizinhos[i];
}

// chamadas de execução principal do script
int main () {

    int n, m;
    int v, w, p;

    // scan dos parâmetros da cidade
    while (scanf("%d %d", &n, &m) != EOF && n && m) {
        contador = 0;
        for (int i = 0; i < n; i++) {
            vizinhos[i] = -1;
            auxiliar[i] = -1;
            adjacentes[i].clear();
        }

        for (int i = 0; i < m; i++) {
            // scan para inserção de arestas informadas 
            scanf("%d %d %d", &v, &w, &p);
            adjacentes[v-1].push_back(w-1);
            if (p == 2) 
                adjacentes[w-1].push_back(v-1);
        }
        
        // chaamda da função recursiva
        buscaprofunda(0);

        int i;
        for (i = 1; i < n && auxiliar[i] > vizinhos[i]; i++);

        // exibição do resultado da análise da cidade
        if (i >= n) printf("1\n");
        else printf("0\n");
    }
}