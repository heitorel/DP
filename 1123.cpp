/*
 * Grupo 20
*/

#include<bits/stdc++.h>

#define INF INT_MAX

using namespace std;

typedef struct{
	int mat[1010][1010];
	int numVertices;
	int numArestas;	
} Grafo;

int distancia[1010];
int antecessor[1010];

queue<int> filaPrioridade;


void inicializaArvore(Grafo* grafo, int ini){
	filaPrioridade.push(ini); 
	for(int i=0; i<=grafo->numVertices; i++){
		distancia[i] = INF;
		antecessor[i] = -1;
	}
	distancia[ini] = 0;
}


void inicializaGrafo(Grafo* g, int numVertices, int numArestas){
	g->numArestas=numArestas;
	g->numVertices=numVertices;
	for(int i=0; i<=g->numVertices; i++){
		for(int j=0;j<=g->numVertices; j++){
			g->mat[i][j] = INF;
		}
	}
}

void relaxaAresta(Grafo* grafo, int u, int v){
	if(distancia[v] > distancia[u] + grafo->mat[u][v]){
		distancia[v] = distancia[u] + grafo->mat[u][v];
		filaPrioridade.push(v);
	}
	
}

void minimizaGrafo(Grafo* grafo, int ini){ //Complexidade de O(av) - se grafo suficientemente denso, O(v^2)
	inicializaArvore(grafo, ini); //O(v)
	while(!filaPrioridade.empty()){ //O(v)
		int i = filaPrioridade.front(); //O(1)
		filaPrioridade.pop(); //O(1)
		int u = 0;
		while(u<grafo->numVertices){ //O(v)
			if(grafo->mat[i][u] != INF)
				relaxaAresta(grafo, i, u); //O(a)
			u++;
		}
	}
	
}

void verificaLocalizacao(Grafo* g, int cidadeU, int cidadeV, int numCidadesRota, int pedagio){
	
	int dif = cidadeU - cidadeV;
	if(cidadeU < numCidadesRota && cidadeV >= numCidadesRota)
		g->mat[cidadeV][cidadeU] = pedagio;
	if(cidadeV < numCidadesRota && cidadeU >= numCidadesRota)
		g->mat[cidadeU][cidadeV] = pedagio;
		
	if(cidadeU >= numCidadesRota && cidadeV >= numCidadesRota){
		g->mat[cidadeU][cidadeV] = pedagio;
		g->mat[cidadeV][cidadeU] = pedagio;
	}
	if(cidadeU < numCidadesRota && cidadeV < numCidadesRota && abs(dif) == 1){
		g->mat[cidadeU][cidadeV] = pedagio;
		g->mat[cidadeV][cidadeU] = pedagio;
	}
		
}


int main (){
	
	int numCidades, numEstradas, numCidadesRota, cidConserto;
	
	do{
		
		scanf("%d", &numCidades);
		scanf("%d", &numEstradas);
		scanf("%d", &numCidadesRota);
		scanf("%d", &cidConserto);
		
		if(numCidades!=0 && numEstradas!=0 && numCidadesRota!=0 && cidConserto!=0){
			Grafo grafo;
			inicializaGrafo(&grafo, numCidades, numEstradas);
			
			
			for(int i=1; i<=grafo.numArestas; i++){ 
				int cidadeU, cidadeV, pedagio;
				scanf("%d", &cidadeU);
				scanf("%d", &cidadeV);
				scanf("%d", &pedagio);
				verificaLocalizacao(&grafo, cidadeU, cidadeV, numCidadesRota, pedagio);
			}
		
			minimizaGrafo(&grafo, cidConserto);
			printf("%d\n", distancia[numCidadesRota-1]); 
		}
		
	}while(numCidades!=0 && numEstradas!=0 && numCidadesRota!=0 && cidConserto!=0);
	
	return 0;
}
