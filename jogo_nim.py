def computador_escolhe_jogada(n, m):
    return estrategia_vencedora(n, m)

def estrategia_vencedora(n, m):
    numero = 0
    aux = 1
    encontrou = False
    while aux < m and not encontrou:
        pecas_deixadas = n - aux
        if pecas_deixadas != 1:
            if (pecas_deixadas % (m + 1)) == 0:
                encontrou = True
                numero = aux
        aux += 1

    if not encontrou:
        numero = m

    return numero

def usuario_escolhe_jogada(n, m):
    pecas = int(input("Quantas peças você vai tirar? "))

    while pecas > m or pecas > n:
        print("Oops! Jogada inválida! Tente de novo.")
        
        pecas = int(input("Quantas peças você vai tirar? "))

    return pecas

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    aux = 0
    jogo_acabou = False
    vencedor = 0 #1-Computador, 2-Usuário

    computador_comeca = True
    if n % (m+1) == 0:
        computador_comeca = False
        print("Voce começa!")
    else:
        print("Computador começa!")

    while n > 0:
        if computador_comeca:
            if not jogo_acabou:
                aux = computador_escolhe_jogada(n, m)
                print("O computador tirou %1d peça" % (aux))
                n -= aux
                if n == 0:
                    jogo_acabou = True
                    vencedor = 1
                    print("Fim do jogo! O computador ganhou!")
                else:
                    print("Agora resta apenas %1d peça no tabuleiro." % (n))

            if not jogo_acabou:
                aux = usuario_escolhe_jogada(n, m)
                print("Você tirou %1d peça" % (aux))
                n -= aux
                if n == 0:
                    jogo_acabou = True
                    vencedor = 2
                    print("Fim do jogo! Você ganhou!")
                else:
                    print("Agora resta apenas %1d peça no tabuleiro." % (n))
        else:
            if not jogo_acabou:
                aux = usuario_escolhe_jogada(n, m)
                print("Você tirou %1d peça" % (aux))
                n -= aux
                if n == 0:
                    jogo_acabou = True
                    vencedor = 2
                    print("Fim do jogo! Você ganhou!")
                else:
                    print("Agora resta apenas %1d peça no tabuleiro." % (n))
            
            if not jogo_acabou:
                aux = computador_escolhe_jogada(n, m)
                print("O computador tirou %1d peça" % (aux))
                n -= aux
                if n == 0:
                    jogo_acabou = True
                    vencedor = 1
                    print("Fim do jogo! O computador ganhou!")
                else:
                    print("Agora resta apenas %1d peça no tabuleiro." % (n))

    return vencedor

def campeonato():
    print("Voce escolheu um campeonato!")

    total_partidas = 3
    n_partida = 1

    n_vitorias_usuario = 0
    n_vitorias_computador = 0

    vencedor = 0

    while n_partida <= total_partidas:
        print("**** Rodada %1d ****" % (n_partida))

        vencedor = partida()
        if vencedor == 1:
            n_vitorias_computador += 1
        elif vencedor == 2:
            n_vitorias_usuario += 1
        
        n_partida += 1

    print("**** Final do campeonato! ****")
    print("Placar: Você %1d X %1d Computador" % (n_vitorias_usuario, n_vitorias_computador))
    

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada;")
    
    escolha_str = input("2 - para jogar um campeonato: ")
    while (escolha_str != "1" and escolha_str != "2"):
        print("Escolha Inválida!")
        print("Bem-vindo ao jogo do NIM! Escolha:")
        print("")
        print("1 - para jogar uma partida isolada;")
        
        escolha_str = input("2 - para jogar um campeonato: ")

    if escolha_str == "1":
        partida()
    elif escolha_str == "2":
        campeonato()

def test_estrategia_vencedora():
    numero = estrategia_vencedora(2, 2)
    assert(numero == 2)

main()
