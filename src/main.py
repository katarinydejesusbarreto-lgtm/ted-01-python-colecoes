def carregar_jogos():
    

    jogos= [{
        'id_jogo': 'J01',
        'nome': 'Aventura X',
        'genero': 'Aventura',
        'plataforma': 'PC',
        'duracao_h': 120
    },{
        'id_jogo': 'J02',
        'nome': 'Mundo Pixel',
        'genero': 'RPG',
        'plataforma': 'PC',
        'duracao_h': 180
    },{
        'id_jogo': 'J03',
        'nome': 'Corrida Turbo',
        'genero': 'Corrida',
        'plataforma': 'Console',
        'duracao_h': 90
    },{
        'id_jogo': 'J04',
        'nome': 'Arena',
        'genero': 'Acao',
        'plataforma': 'Console',
        'duracao_h': 110
    
    }, {
        'id_jogo': 'J05',
        'nome': 'Estrategia 9',
        'genero': 'Essencial',
        'plataforma': 'PC',
        'duracao_h': 200
    
    }, {
        'id_jogo': 'J06',
        'nome': 'Futebol Pro',
        'genero': 'Esportes',
        'plataforma': 'Console',
        'duracao_h': 100
    
    }, {
        'id_jogo': 'J07',
        'nome': 'Misterio',
        'genero': 'Suspense',
        'plataforma': 'PC',
        'duracao_h': 130
    
    },{
        'id_jogo': 'J08',
        'nome': 'Galaxia',
        'genero': 'Ficicao',
        'plataforma': 'Console',
        'duracao_h':150 
    }]

    return jogos
def carregar_vendas():


    vendas = []

    with open('dados/vendas.csv', 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    linhas = linhas[1:]

    for linha in linhas:

        dados = linha.split(",")

        venda = {
            'id_venda': dados[0],
            'id_jogo': dados[1],
            'quantidade': int(dados[2]),
            'avaliacao': float(dados[3])
        }

        vendas.append(venda)

    return vendas

def mostrar_jogos_mais_vendidos(jogos, vendas):
    totais= {}
    jogos_por_id = {
        jogo['id_jogo']: jogo['nome']
        for jogo in jogos
    }

    mais_vendido = ''
    maior_total = 0

    for venda in vendas:

        id_jogo = venda['id_jogo']
        quantidade = venda['quantidade']

        if id_jogo in totais:
            totais[id_jogo] += quantidade
        else:
            totais[id_jogo] = quantidade
  

    print('\n JOGOS MAIS VENDIDOS')
    print('---------------------')
    for id_jogo, total in totais.items():

        for jogo in jogos:
             
             if jogo['id_jogo'] == id_jogo:

                print(jogo['nome'], '-', total, 'unidades')

                if total> maior_total:
                    maior_total= total
                    mais_vendido= jogo['nome']

    print('\n JOGO MAIS VENDIDO')
    print('--------------------')
    print(mais_vendido, '-', maior_total, 'unidades')

def calcular_media_avaliacao(jogos, vendas):
    somas= {}
    contagens= {}

    for venda in vendas:
        id_jogo= venda['id_jogo']
        avaliacao= venda['avaliacao']

        for jogo in jogos:
            if jogo['id_jogo'] == id_jogo:
                genero= jogo['genero']

                if genero in somas:
                    somas[genero] += avaliacao
                    contagens[genero] += 1
                else:
                    somas[genero]= avaliacao
                    contagens[genero] = 1

    print('\n MÉDIA DE AVALIAÇÃO POR GÊNERO')
    print('--------------------------------')

    for genero in somas:
        media= somas[genero]/contagens[genero]
        print(genero, '-', round(media,2))

def calcular_media_plataforma(jogos, vendas):

    somas= {}
    contagens= {}

    for venda in vendas:

        id_jogo= venda['id_jogo']
        avaliacao= venda['avaliacao']

        for jogo in jogos:

            if jogo['id_jogo'] == id_jogo:
                plataforma= jogo['plataforma']

                if plataforma in somas:
                    somas[plataforma] += avaliacao
                    contagens[plataforma] += 1

                else:
                    somas[plataforma]= avaliacao
                    contagens[plataforma] = 1


    print('\n MÉDIA DE AVALIAÇÃO POR PLATAFORMA')
    print('------------------------------------')


    for plataforma in somas:
        media= somas[plataforma]/ contagens[plataforma]
        print(plataforma, '-', round(media, 2))


def comparar_plataformas(jogos):
    jogos_pc = [
        jogo['nome']
        for jogo in jogos
        if jogo['plataforma'] == 'PC'
    ]

    jogos_console = [
        jogo['nome']
        for jogo in jogos
        if jogo['plataforma'] == 'Console'
    ]

    generos_pc = set()
    generos_console = set()

    for jogo in jogos:

        if jogo['plataforma'] == 'PC':
            generos_pc.add(jogo['genero'])

        else:
            generos_console.add(jogo['genero'])

    comuns = generos_pc.intersection(generos_console)

    print('\nJOGOS PC')
    print(jogos_pc)

    print('\nJOGOS CONSOLE')
    print(jogos_console)

    print('\nGENEROS EM COMUM')
    if len(comuns)>0:
        print(comuns)
    else:
        print('NENHUM GÊNERO EM COMUM ENCONTRADO')
   

print('Programa Iniciado')

jogos= carregar_jogos()

print(len(jogos))

vendas= carregar_vendas()
print(len(vendas))

mostrar_jogos_mais_vendidos(jogos, vendas)
calcular_media_avaliacao(jogos, vendas)
calcular_media_plataforma(jogos, vendas)
comparar_plataformas(jogos)
