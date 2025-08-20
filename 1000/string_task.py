s = input()
minus = s.lower()
vocales = "aeiouy"
sinvocal = "".join(l for l in minus if l not in vocales)
conpuntos = "".join("." + l for l in sinvocal)
print(conpuntos)
