import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0.0
    for i in range(len(as_a)):
        soma += (as_a[i] - as_b[i])

    return abs(soma) / len(as_a)

def calcula_tamanho_medio_palavra(lista_palavra):
    '''Essa funcao recebe uma lista de palavras e devolve a soma dos tamanhos das palavras dividida pelo número total de palavras.'''
    soma = 0

    for palavra in lista_palavra:
        soma += len(palavra)

    return soma/len(lista_palavra)

def calcula_tamanho_medio_sentenca(sentencas):
    '''Essa funcao recebe uma lista de sentencas e devolve a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças'''
    soma = 0.0
    for sentenca in sentencas:
        soma += len(sentenca)

    return soma/len(sentencas)

def calcula_complexidade_sentenca(sentencas):
    '''Essa funcao recebe uma lista de sentencas e devolve a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças'''
    n_frases = 0
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        n_frases += len(frases)

    return n_frases/len(sentencas)

def calcula_tamanho_medio_frase(sentencas):
    '''Essa funcao recebe uma lista de sentencas e devolve a soma do número de caracteres em cada frase dividida pelo número de frases no texto'''
    n_caracteres = 0
    n_frases = 0
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        n_frases += len(frases)
        for frase in frases:
            n_caracteres += len(frase)

    return n_caracteres/n_frases

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = 0 # Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    ttr = 0 # Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    hlr = 0 # Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
    sal = 0 # Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    sac = 0 # Complexidade de sentença: Média simples do número de frases por sentença.
    pal = 0 # Tamanho médio de frase: Média simples do número de caracteres por frase.

    palavras = []

    sentencas = separa_sentencas(texto)
    n_sentencas = len(sentencas)
    n_palavras = 0

    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras_frases = separa_palavras(frase)
            palavras += palavras_frases

    n_palavras = len(palavras)

    wal = calcula_tamanho_medio_palavra(palavras)

    ttr = n_palavras_diferentes(palavras)/n_palavras

    hlr = n_palavras_unicas(palavras)/n_palavras

    sal = calcula_tamanho_medio_sentenca(sentencas)

    sac = calcula_complexidade_sentenca(sentencas)

    pal = calcula_tamanho_medio_frase(sentencas)

    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    graus = []
    ass = 0.0
    grau = 0.0
    for texto in textos:
        ass = calcula_assinatura(texto)
        grau = compara_assinatura(ass, ass_cp)
        graus.append(grau)

    return avalia_grau_similaridade(graus)

def avalia_grau_similaridade(graus):
    '''Essa funcao recebe uma lista de graus e deve devolver o numero (1 a n) do graus mais próximo.'''
    dif = max(graus)
    n_grau_similar = 0
    for i in range(len(graus)):
        if graus[i] < dif:
            dif = graus[i]
            n_grau_similar = i
    return n_grau_similar + 1

def main():
    ass_cp = le_assinatura()
    textos = le_textos()

    n = avalia_textos(textos, ass_cp)

    print("O autor do texto %1d está infectado com COH-PIAH" % (n))

def test_texto():
    #Comparando assinaturas do textos(ass1=[4.34, 0.05, 0.02, 12.81, 2.16, 0.0], ass2=[3.96, 0.05, 0.02, 22.22, 3.41, 0.0]) - Falhou ** ** *
    #AssertionError: Esperado: 1.84; recebido: 1.713

    wal = 4.79
    ttr = 0.72
    hlr = 0.56
    sal = 80.5
    sac = 2.5
    pal = 31.6

    as_p = [wal, ttr, hlr, sal, sac, pal]

    texto1 = "Navegadores antigos tinham uma frase gloriosa:\"Navegar é preciso; viver não é preciso\". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."
    texto2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
    texto3 = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."

    as_1 = calcula_assinatura(texto1)
    as_2 = calcula_assinatura(texto2)
    as_3 = calcula_assinatura(texto3)

    grau_1 = compara_assinatura(as_1, as_p)
    grau_2 = compara_assinatura(as_2, as_p)
    grau_3 = compara_assinatura(as_3, as_p)

    print("Grau 1", grau_1)
    print("Grau 2", grau_2)
    print("Grau 3", grau_3)

    lista = [grau_1, grau_2, grau_3]
    n_texto = avalia_grau_similaridade(lista)
    print("", n_texto)

    assert(n_texto, 1)

main()