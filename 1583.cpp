/*
 * Grupo 20
*/

#include <iostream>
#include <vector>

using namespace std;

int nLinhas, nColunas;
vector<vector<char>> mapa;

void floodFill(int i, int j) {
    // Casos base
    if (i >= nLinhas || j >= nColunas || i < 0 || j < 0)
        return;
    if (mapa[i][j] != 'A')
        return;
    else if (mapa[i][j] == 'A')
        mapa[i][j] = 'T';

    // Recursao
    floodFill(i + 1, j);
    floodFill(i - 1, j);
    floodFill(i, j + 1);
    floodFill(i, j - 1);
}

int main() {
    // Vetores que vao guardar as posicoes dos elementos contaminados
    vector<int> linhaElementosT;
    vector<int> colunaElementosT;

    while (true) {
        cin >> nLinhas >> nColunas;

        // Caso final
        if (nLinhas == 0 && nColunas == 0)
            break;

        // Input do mapa
        for (int i = 0; i < nLinhas; ++i) {
            vector<char> linha;
            char c;

            for (int j = 0; j < nColunas; ++j) {
                cin >> c;

                // Caso quando elemento for contaminado
                if (c == 'T') {
                    c = 'A';

                    // Adiciona elemento contaminado nos Vetores
                    linhaElementosT.push_back(i);
                    colunaElementosT.push_back(j);
                }

                // Adiciona cada elemento em uma linha
                linha.push_back(c);
            }
            // Adiciona a linha na matriz do mapa
            mapa.push_back(linha);

            linha.clear();
        }

        // Chama funcao de preenchimento para cada elemento contaminado
        for (int i = 0; i < colunaElementosT.size(); i++)
            floodFill(linhaElementosT[i], colunaElementosT[i]);


        // Exibe matriz do mapa preenchido
        for (int i = 0; i < nLinhas; ++i) {
            for (int j = 0; j < nColunas; ++j) {
                cout << mapa[i][j];
            }
            cout << endl;
        }
        cout << endl;

        // Reseta matriz e vetores
        for (auto & linha : mapa) {
            linha.clear();
        }
        mapa.clear();
        linhaElementosT.clear();
        colunaElementosT.clear();
    }

    return 0;
}
