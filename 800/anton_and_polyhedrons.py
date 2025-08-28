n = int(input())
p = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}
faces = 0
for _ in range(n):
    faces += p[input()]
print(faces)
