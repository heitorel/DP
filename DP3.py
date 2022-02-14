# Heitor Bianchi - 12058730
# Matheus Silvério - 10258921

# o scripc recebe uma função e mantém uma variável de controle "parenteses"
# um laço lê essa função e sempre que um parenteses é  fechado sem abrir retorna "incorrect"
# se ao final da leitura a variável de controle for negativa ent]ap abriu-se mais do que fechou-se 
# portanto retorna "incorrect"

import sys

entrace = '''public boolean checkCollision(Wall wall){        if (wall.getId() == "Bottom")        {            if ((this.cy + (this.height / 2.0) >= (wall.get() - (wall.getHeight() / 2.0))))        } else if (wall.getId() == "Top")        {            if ((this.cy -(this.height / 2.0)) <= (wall.getCy() + (wall.getHeight() / 2.0))) return true;         } else if (wall.getId() == "Left")         {            if ((this.cx - (this.width / 2.0)) <= (wall.getCx() + (wall.getWidth() / 2.0 ))) return true;        } else if (wall.getId() / 2.0 == "Right")         {            if ((this.cx + (this.width / 2.0)) >= (wall.getCx() - (wall.getWidth() / 2.0))) return true;        }       return false;    }'''.strip().split('\n')

for l in entrace:
    parenteses = 0
    for letra in l:
        if letra == '(':
            parenteses = parenteses + 1
        if letra == ')':
            parenteses = parenteses - 1
        if parenteses < 0:
            print('incorrect \n')
            break
    if parenteses > 0:
        print('incorrect \n')
    else:
        print('correct \n')

