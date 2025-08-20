s = input()
count = 1
i = 0
j = 1
while j < len(s):
    if s[i] == s[j]:
        count += 1
        j += 1
        if count == 7:
            print("YES")
            exit()
    else:
        i = j
        j = i + 1
        count = 1
print("NO")


def is_dangerous(s: str) -> str:
    """
    Devuelve 'YES' si hay 7 (o más) iguales consecutivos en s; en caso contrario 'NO'.
    Lógica: contar la longitud de la racha actual y verificar si llega a 7.
    """
    streak = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            streak += 1
            if streak >= 7:
                return "YES"
        else:
            streak = 1
    return "YES" if len(s) >= 1 and streak >= 7 else "NO"
    # Nota: la línea anterior es redundante por el return dentro del bucle;
    # se deja por claridad si el string fuera muy corto.


def is_dangerous(s: str) -> str:
    return "YES" if ("0000000" in s or "1111111" in s) else "NO"
