n = int(input())
monedas = list(map(int, input().split()))
monedas.sort(reverse=True)
total = sum(monedas)
tomadas = 0
suma = 0
for cantidad, moneda in enumerate(monedas, start=1):
    suma += moneda
    if suma > total - suma:
        print(cantidad)
        break
