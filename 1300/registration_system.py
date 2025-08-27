# n = int(input())

# bd = set()
# i = 1
# for _ in range(n):
#     name = input()
#     if name not in bd:
#         bd.add(name)
#         print("OK")
#     else:
#         while True:
#             new_name = name + str(i)
#             if new_name not in bd:
#                 bd.add(new_name)
#                 print(new_name)
#                 break
#             else:
#                 i += 1

n = int(input())

database = set()
indice = {}

for _ in range(n):
    name = input()
    if name not in database:
        database.add(name)
        indice[name] = 1
        print("OK")
    else:
        i = indice.get(name)
        new_name = name + str(i)
        database.add(new_name)
        i += 1
        indice[name] = i
        print(new_name)
