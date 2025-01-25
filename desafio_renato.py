def kg_para_mg(kg):
    return kg * 1_000_000

def kg_para_g(g):
    return g * 1_000

kg = int(input("Número : "))
kg = kg  # Quantidade em kg
mg = kg_para_mg(kg)
print(f"{kg} kg é igual a {mg} mg")

g = int(input("Número : "))
g = g  # Quantidade em g
g = kg_para_g(kg)
print(f"{kg} kg é igual a {g} g")