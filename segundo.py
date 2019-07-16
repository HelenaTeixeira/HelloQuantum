#Helena Teixeira - 93720
#primeiro semestre - FP 
#dev ready
#CELULAS
def cria_celula(x):
    '''
    cria_celula:{-1,0,1} --- celula
        funcao que recebe o valor do estado do qubit (-1,0,1) e retorna uma celula com esse valor
        a minha representacao interna e com dicionarios em que as chaves sao incerto, ativo e inativo
        e o valor c o estado do qubit
    '''
    if type(x)!= int or x not in (-1, 0, 1):
        raise ValueError("cria_celula: argumento invalido.")
    elif x ==0:
        return {"inativo":x}
    elif x ==1:
        return {"ativo":x}
    else:
        return {"incerto":x}

def obter_valor(c):
    '''
    obter_valor: celula --- {1,0,-1}
        funcao que devolve o valor associado a celula
    '''
    for e in c:
        return c[e]

def inverte_estado(c):
    '''
    inverte_estado: celula --- celula
        funcao que inverte o estado da celula (se for -1 nao ha alteracoes)
    '''
    if "inativo" in c:
        c.clear()
        c["ativo"] = 1
    elif "ativo" in c:
        c.clear()
        c["inativo"] = 0
    return c

def eh_celula(c):
    '''
    eh_celula: universal --- logico
        funcao que retorna verdadeiro se o argumento for do tipo celula
    '''
    return isinstance(c,dict) and len(c)==1 and c in ({"inativo":0},{"ativo":1},{"incerto":-1})

def celulas_iguais(c1,c2):
    '''
    celulas_iguais: celula x celula --- logico
        funcao que retorna verdadeiro se as duas celulas estao no mesmo estado
    '''
    return eh_celula(c1) and eh_celula(c2) and obter_valor(c1) == obter_valor(c2)

def celula_para_str(c):
    '''
    celula_para_str: celula --- cadeia de caracteres
        funcao que com uma cadeia de caracteres representa a celula dada
    '''
    if obter_valor(c) == -1:
        return "x"
    else:
        return str(obter_valor(c))

#COORDENADA
def cria_coordenada(l,c):
    '''
    cria_coordenada: n x n --- coordenada
        funcao que devolve a coordenada correspondente a linha e coluna
        a minha representacao interna e um dicionario com dois elementos em que
        a primeira chave e linha(com o valor correspondente a linha) e
        a segunda chave e coluna (com o valor correspondente a coluna)
    '''
    if type(l) != int or type(c)!= int or l not in (0,1,2) or c not in (0,1,2):
        raise ValueError("cria_coordenada: argumentos invalidos.")
    else:
        return {"linha":l,"coluna":c}

def coordenada_linha(c):
    '''
    coordenada_linha: coordenada --- n
        funcao que retorna o natural correspondente a linha da coordenada
    '''
    return c["linha"]

def coordenada_coluna(c):
    '''
    coordenada_coluna: coordenada --- n
        funcao que retorna o natural correspondente a coluna da coordenada
    '''
    return c["coluna"]

def eh_coordenada(arg):
    '''
    eh_coordenada: universal --- logico
        funcao que retorna verdadeiro apenas quando o seu argumento e do tipo coordenada
    '''
    return isinstance(arg,dict) and len(arg)==2 and\
           all(type(arg[c])== int and c in ("linha","coluna")and arg[c] in (0,1,2) for c in arg)

def coordenadas_iguais(c1,c2):
    '''
    coordenadas_iguais: coordenada x coordenada --- logico
        funcao que retorna verdadeiro se os argumentos forem coordenadas da mesma posicao
    '''
    return eh_coordenada(c1) and eh_coordenada(c2) and coordenada_linha(c1)== coordenada_linha(c2) and\
           coordenada_coluna(c1)== coordenada_coluna(c2)

def coordenada_para_str(c):
    '''
    coordenada_para_str: coordenada --- cadeia de caracteres
        funcao que retorna a cadeia de caracteres que represnta a coordenada
    '''
    return "("+ str(coordenada_linha(c))+", "+ str(coordenada_coluna(c))+")"

#TABULEIROS
def lista_coord():
    '''
    lista_coord: {} --- lista
        funcao auxiliar que retorna uma lista com as coordenadas existentes no tabuleiro
    '''
    return [cria_coordenada(0,0),cria_coordenada(0,1),cria_coordenada(0,2),\
            cria_coordenada(1,0),cria_coordenada(1,1), cria_coordenada(1,2),\
            cria_coordenada(2,1),cria_coordenada(2,2)]

def tabuleiro_inicial():
    '''
    tabuleiro_inicial: {} --- tabuleiro
        funcao que retorna o tabuleiro com o estado inicial do jogo
        a minha representacao interna e dicionario em que cada elemento tem a chave como a cadeia de caracteres
        que corresponde as coordenadas e tem valor como a celula correspondente a essa coordenada no tabuleiro
    '''
    return {coordenada_para_str(cria_coordenada(0,0)):cria_celula(-1),coordenada_para_str(cria_coordenada(0,1)):cria_celula(-1),\
            coordenada_para_str(cria_coordenada(0,2)):cria_celula(-1),coordenada_para_str(cria_coordenada(1,0)):cria_celula(0),\
            coordenada_para_str(cria_coordenada(1,1)):cria_celula(0),coordenada_para_str(cria_coordenada(1,2)):cria_celula(-1), \
            coordenada_para_str(cria_coordenada(2,1)): cria_celula(0),coordenada_para_str(cria_coordenada(2,2)):cria_celula(-1)}

def str_para_tabuleiro(s):
    '''
    str_para_tabuleiro: cadeia de caracteres --- tabuleiro
        funcao que retorna o tabuleiro correspondente a cadeia de caracteres do argumento
    '''
    if not isinstance(s,str) or s[0]!="(" or s[-1]!= ")" or len(eval(s))!= 3 or\
        any([len(eval(s)[i])!= (3,3,2)[i] or type(eval(s)[i]) != tuple and all(j in (-1,0,1) for j in eval(s)[i]) for i in range(3)]):
        raise ValueError("str_para_tabuleiro: argumento invalido.")
    return {coordenada_para_str(cria_coordenada(0, 0)): cria_celula(eval(s)[0][0]),coordenada_para_str(cria_coordenada(0, 1)): cria_celula(eval(s)[0][1]),\
            coordenada_para_str(cria_coordenada(0, 2)): cria_celula(eval(s)[0][2]),coordenada_para_str(cria_coordenada(1, 0)): cria_celula(eval(s)[1][0]),\
            coordenada_para_str(cria_coordenada(1, 1)): cria_celula(eval(s)[1][1]),coordenada_para_str(cria_coordenada(1, 2)): cria_celula(eval(s)[1][2]),\
            coordenada_para_str(cria_coordenada(2, 1)): cria_celula(eval(s)[2][0]),coordenada_para_str(cria_coordenada(2, 2)): cria_celula(eval(s)[2][1])}

def tabuleiro_dimensao(t):
    '''
    tabuleiro_dimensao: tabuleiro --- n
        funcao que retorna o numero de linhas(ou seja colunas tambem)
    '''
    return 3

def tabuleiro_celula(t,coor):
    '''
    tabuleiro_celula: tabuleiro x coordenada --- celula
        funcao que devolve a celula associada a coordenada do tabuleiro nos argumentos
    '''
    return t[coordenada_para_str(coor)]

def tabuleiro_substitui_celula(t,cel,coor):
    '''
    tabuleiro_substitui_celula: tabuleiro x celula x coordenada --- tabuleiro
        funcao que retorna o tabuleiro que resulta da substituicao da celula existente na coordenada
        do argumento pela nova celula dada no argumento
    '''
    if not eh_tabuleiro(t) or not eh_celula(cel) or not eh_coordenada(coor):
        raise ValueError("tabuleiro_substitui_celula: argumentos invalidos.")
    else:
        t[coordenada_para_str(coor)]= cel
        return t

def tabuleiro_inverte_estado(t,coor):
    '''
    tabuleiro_inverte_estado: tabuleiro x coordenada --- tabuleiro
        funcao que retorna o tabuleiro depois de inverter o estado da celula na coordenada (dos argumentos)
    '''
    if not eh_tabuleiro(t) or not eh_coordenada(coor):
        raise ValueError("tabuleiro_inverte_estado: argumentos invalidos.")
    inverte_estado(tabuleiro_celula(t,coor))
    return t

def eh_tabuleiro(arg):
    '''
    eh_tabuleiro: universal --- logico
        funcao que retorna verdadeiro se o argumento for do tipo tabuleiro
    '''
    return isinstance(arg,dict) and len(arg)==8 and all(eh_celula(arg[c]) for c in arg)

def tabuleiros_iguais(t1,t2):
    '''
    tabuleiros_iguais: tabuleiro x tabuleiro --- logico
        funcao que retorna verdadeiro se os argumentos forem tabuleiros que tenham as mesmas celulas em cada uma das coordenadas
    '''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and\
           all(celulas_iguais(tabuleiro_celula(t1,c), tabuleiro_celula(t2,c)) for c in lista_coord())

def tabuleiro_para_str(t):
    '''
    tabuleiro_para_str: tabuleiro --- cadeia de caracteres
        funcao que retorna a cadeia de caracteres que representa o seu argumento
    '''
    return '+-------+\n|...{2}...|\n|..{1}.{5}..|\n|.{0}.{4}.{7}.|\n|..{3}.{6}..|\n+-------+'.format(*[celula_para_str(tabuleiro_celula(t,e)) for e in lista_coord()])

#PORTAS

def porta_x(t,l):
    '''
    porta_x: tabuleiro x {"E","D"} --- tabuleiro
        Funcao que conssoante seja esquerda ou direita aplica a porta x
        ( inverte as celulas das diagonais de dentro do tabuleiro)
    '''
    if not eh_tabuleiro(t) or l not in ("E","D"):
        raise ValueError("porta_x: argumentos invalidos.")
    elif l == "E":
        tabuleiro_inverte_estado(t,cria_coordenada(1,0))
        tabuleiro_inverte_estado(t,cria_coordenada(1,1))
        tabuleiro_inverte_estado(t,cria_coordenada(1,2))
        return t
    elif l =="D":
        tabuleiro_inverte_estado(t,cria_coordenada(2,1))
        tabuleiro_inverte_estado(t,cria_coordenada(1,1))
        tabuleiro_inverte_estado(t,cria_coordenada(0,1))
        return t

def porta_z(t,l):
    '''
    porta_z: tabuleiro x {"E","D"} --- tabuleiro
        funcao que que conssoante seja esquerda ou direita aplica a porta z
        ( inverte as celulas das diagonais de fora do tabuleiro)
    '''
    if not eh_tabuleiro(t) or l not in ("E","D"):
        raise ValueError("porta_z: argumentos invalidos.")
    elif l=="E":
        tabuleiro_inverte_estado(t,cria_coordenada(0,0))
        tabuleiro_inverte_estado(t,cria_coordenada(0,1))
        tabuleiro_inverte_estado(t,cria_coordenada(0,2))
        return t
    elif l =="D":
        tabuleiro_inverte_estado(t,cria_coordenada(2,2))
        tabuleiro_inverte_estado(t,cria_coordenada(1,2))
        tabuleiro_inverte_estado(t,cria_coordenada(0,2))
        return t

def troca_aux(t,coor1, coor2):
    '''
    troca_aux: tabuleiro x coordenada x coordenada --- tabuleiro
        funcao que auxilia a porta_h trocando as celulas de duas coordenadas dadas
    '''
    coorin = tabuleiro_celula(t, coor2)
    tabuleiro_substitui_celula(t, tabuleiro_celula(t, coor1), coor2)
    tabuleiro_substitui_celula(t, coorin, coor1)
    return t

def porta_h(t,l):
    '''
    porta_h: tabuleiro x {"E","D"} --- tabuleiro
        funcao que conssoante seja esquerda ou direita aplica a porta h
        ( troca as duas diagonais de cada lado do tabuleiro) com a funcao troca_aux
    '''
    if not eh_tabuleiro(t) or l not in ("E","D"):
        raise ValueError("porta_h: argumentos invalidos.")
    elif l== "E":
        troca_aux(t,cria_coordenada(0,0),cria_coordenada(1,0))
        troca_aux(t,cria_coordenada(0,1),cria_coordenada(1,1))
        troca_aux(t,cria_coordenada(0,2),cria_coordenada(1,2))
        return t
    elif l == "D":
        troca_aux(t,cria_coordenada(0,1),cria_coordenada(0,2))
        troca_aux(t,cria_coordenada(1,1),cria_coordenada(1,2))
        troca_aux(t,cria_coordenada(2,1),cria_coordenada(2,2))
        return t

#FUNCAO ADICIONAL

def hello_quantum(s):
    '''
    hello_quantum: cadeia de caracteres --- logico
        funcao que recebe uma cadeia de caracteres com o tabuleiro objetivo e o numero maximo de jogadas
        retorna verdadeiro se o jogador conseguir transformar o tabuleiro inicial
        no tabuleiro objetivo no numero de jogadas indicado
    '''
    partes = s.split(":")
    print("Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:\n",tabuleiro_para_str(str_para_tabuleiro(partes[0])),\
          "\nComecando com o tabuleiro que se segue:\n",tabuleiro_para_str(tabuleiro_inicial()),sep = "")
    contador_jogadas = 0
    t = tabuleiro_inicial()
    while contador_jogadas != int(partes[1]):
        p = input("Escolha uma porta para aplicar (X, Z ou H): ")
        l = input("Escolha um qubit para analisar (E ou D): ")
        if p == "X":
            porta_x(t,l)
        elif p == "Z":
            porta_z(t,l)
        else:
            porta_h(t,l)
        print(tabuleiro_para_str(t))
        contador_jogadas += 1
    if tabuleiros_iguais(t,str_para_tabuleiro(partes[0])):
        print("Parabens, conseguiu converter o tabuleiro em", partes[1], "jogadas!")
        return True
    else:
        return False




