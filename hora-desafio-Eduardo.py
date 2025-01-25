#sistema de notas
print("------- SISTEMA ESCOLAR----------")
notaUm = float(input("Digite nota 1º: "))
notaDois = float(input("Digite nota 2º "))
notaTres = float(input("Digite nota 3º: "))
notaQuatro = float(input("Digite nota 4º "))
media = (notaUm + notaDois + notaTres + notaQuatro) /4
print("---------------------------------")
print("")

#exibir dados
print("------- BOLETIM ESCOLAR ----------")
print("Seja bem vindo(a)!")
print(f"NOTA 1º: {notaUm}\n" #\n quebra de linha
f"NOTA 2º: {notaDois}\n"
f"NOTA 3º: {notaTres}\n"
f"NOTA 4º {notaQuatro}\n\n"
f"MÉDIA: {media}")
print("----------------------------------")

if media >= 7:
    print(f"APROVADO: {media}")
else:
    print(f"REPROVADO: {media}")