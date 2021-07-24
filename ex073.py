# crie uma tupla com os 20 primeiros colocados do brasileirão, na ordem de colocação. Depois mostre:
# A) apenas os 5 primeiros colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está a Chape
brasil = ('Palmeiras', 'Atlético-MG', 'Fortaleza', 'Bragantino', 'Athletico PR', 'Flamengo', 'Ceará', 'Bahia', 'Fluminense',
         'Santos', 'Atlético - Go', 'Corinthians', 'Internacional', 'Juventude', 'Cuiabá', 'São Paulo', 'Sport Recife', 'América MG',
        'Grêmio', 'Chapecoense')
print(brasil[:5])
print(brasil[16:20])
print(sorted(brasil))
print(brasil.index('Chapecoense') + 1)
