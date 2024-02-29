# Colheita de Frutos - FuP 14/03/2023

frutos_climatericos = ['Banana', 'Manga', 'Mamao', 'Maracuja', 'Goiaba', 'Abacate', 'Atemoia', 'Pinha', 'Caqui', 'Maça', 'Pera',
                      'Pessego', 'Ameixa', 'Goiaba', 'Damasco']

frutos_n_climatericos = ['Laranja', 'Limao', 'Tanjerina', 'Uva', 'Abacaxi', 'Morango', 'Roma', 'Carambola', 'Figo', 'Cereja',
                        'Melancia', 'Franboesa', 'Caju', 'Nespera', 'Melao']

mais_vendidos = ['Laranja', 'Mamao', 'Maça', 'Melancia', 'Limao', 'Tangerina', 'Manga', 'Abacaxi']
# -------------------------------------------------------------------------------------------------------------------

meus_climatericos = []
meus_n_climatericos = []
meus_mais_vendidos = []
num_climat = num_n_climat = num_mais_vendidos = 0
quant_climat = quant_n_climat = 0
aux = []
eh_climaterico = ''

# Recebe o ano
while True:
    try:
        ano = int(input('Informe o ano da colheita: '))
        if ano > 0: 
            break
        else:
            print('Digite um ano valido.')
    except ValueError:
        print('Invalido.')

print('DIGITE 0 para terminar o programa')
while True:        
    print('Informe a fruta e sua respectiva quantidade: ')
    # Recebe a fruta
    while True: 
        fruta = input('Fruta: ').capitalize()
        
        if fruta in mais_vendidos: 
            if fruta not in meus_mais_vendidos:
                meus_mais_vendidos.append(fruta)
                num_mais_vendidos += 1 

        if fruta in frutos_climatericos:
            if fruta not in meus_climatericos:
                meus_climatericos.append(fruta)
                num_climat += 1
            break

        elif fruta in frutos_n_climatericos:
            if fruta not in meus_n_climatericos:
                meus_n_climatericos.append(fruta)
                num_n_climat += 1
            break

        else:
            print('Fruta invalida.')

    # Recebe sua quantidade
    while True:
        # quantidade esta em toneladas 
        quantidade = int(input('Quantidade (em toneladas): '))
        if quantidade > 0:
            if fruta in frutos_climatericos:
                quant_climat += quantidade
                break
            elif fruta in frutos_n_climatericos:
                quant_n_climat += quantidade
                break
        else:
            print('Quantidade invalida. ') 

    aux.append((fruta, quantidade))

    resposta = int(input('Continuar? 0 para terminar de inserir frutas. 1 para continuar.'))
    if resposta == 0:
        break
    # qualquer outro numero de resposta, o programa continua

# DESCOBRIR FRUTA QUE FOI MENOS COLHIDA 
menor_j = 100000000000000000
for i, j in aux:
    if j < menor_j:
        menor_j = j # quantidade
        menor_i = i # fruta menos vendida

# DESCOBRIR MAIS VENDIDO 
maior_j = 0
for i, j in aux:
    if j > maior_j:
        maior_j = j # quantidade
        maior_i = i # fruta mais vendida

# EXECUÇÃO 
print()
print(f'Ano: {ano}')
if num_climat == 1:
    print(f'{num_climat} fruto climaterico: ')
else: 
    print(f'{num_climat} frutos climatericos: ')

if num_climat > 0:
    for n in meus_climatericos:
        print(n)
print(f'Quantidade total (em kg) de frutos climatéricos: {quant_climat*1000}\n')

if num_n_climat == 1:
    print(f'{num_n_climat} fruto não climaterico: ')
else:
    print(f'{num_n_climat} frutos não climatericos: ')

if num_n_climat > 0:
    for n in meus_n_climatericos:
        print(n)
print(f'Quantidade total (em kg) de frutos não climatéricos: {quant_n_climat*1000}\n')

if num_mais_vendidos == 0: 
    print(f'Dentre os frutos da colheita de {ano} que estão dentre os mais vendidos não tivemos nenhum fruto.')
else:
    print(f'Dentre os frutos da colheita de {ano} que estão dentre os mais vendidos temos {num_mais_vendidos} frutos, os quais são:')
    for i in meus_mais_vendidos:
        print(i)

print()
print(f'Fruto mais vendido dessa colheita específica: {maior_i} - {maior_j*1000} kg.\n')

if menor_i in frutos_climatericos:
    eh_climaterico = 'climatérico'
elif menor_i in frutos_n_climatericos:
    eh_climaterico = 'não climáterico'

print(f'O {menor_i} que é um fruto {eh_climaterico} teve a menor quantidade colhida, a qual foi: {menor_j*1000} kg')