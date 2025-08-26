# p_inicial = int(input())
# tasa_crecimiento = float(input())
# dias = int(input())

# p_final = int(p_inicial * (tasa_crecimiento**dias))
# print(p_final)

p_inicial = int(input())
tasa = float(input())
dias = int(input())

p_final = p_inicial
for _ in range(dias):
    p_final = round(p_final * tasa)
print(p_final)
