#Criando um programa que calcula quantos litros abastecer no valor de R$6,50

def combustivelValor(combustivel, valor):
    return combustivel * valor
##############################################
def linha(quantidade):
    return '=' * quantidade
##############################################
def cabecalho(texto,quantidade):
    saida = (f'{linha(quantidade)}\n'
             f'{texto.center(quantidade)}\n'
             f'{linha(quantidade)}')
    return saida
##############################################

print('Insira a quantidade de litros que deseja abastecer.\n'
      'Valor do litro R$6,50')

abastecimento = float(input('Quantos litros? '))

print(cabecalho('RECIBO',30))
print(f'Produto: Gasolina\n'
      f'Quantidade de litros: {abastecimento}l\n'
      f'Valor da compra: R${combustivelValor(abastecimento,6.5):.2f}')


