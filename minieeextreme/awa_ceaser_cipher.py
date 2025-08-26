s = input()
k = int(input())

output = ""
for ch in s:
    x = ord(ch)
    print(x)
    if 65 <= x <= 90 and 97 <= x <= 120:
        output += chr(x + k)
    else:
        output += ch

print(output)
