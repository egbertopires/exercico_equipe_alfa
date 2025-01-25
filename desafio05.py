def ePar(fim):
    numerosPares = []
    for numero in range (0,fim+1):
        ehPar = numero % 2
        if not ehPar:
            numerosPares.append(numero)
    saida = 'Numeros pares: '
    for valor in numerosPares:
        saida += f'{valor},'

    return saida[:-1]

print(ePar(15))