matriz = [[0,0],[0,0]]

for l in range (0,2):
    for c in range (0,2):
      matriz [l][c] = int(input(f"insira dois: "))

      print('-='*20)
for l in range (0,2):
     for c in range (0,2):
          print(f"[{matriz[l][c]:^5}]", end="")
     print()

matriz2 = [[0,0],[0,0]]

for l in range (0,2):
    for c in range (0,2):
      matriz2 [l][c] = int(input(f"insira dois valores: "))

print('-='*20)
for l in range (0,2):
     for c in range (0,2):
          print(f"[{matriz2[l][c]:^5}]", end="")
     print()


soma_matrizes =[[0,0],[0,0]]

for l in range (0,2):
    for c in range (0,2):
        soma_matrizes[l][c] = matriz[l][c] * matriz2[l][c]
        print('-=' * 20)
print("Resultado da soma das matrizes:")
for l in range(2):
    for c in range(2):
        print(f"[{soma_matrizes[l][c]:^5}]", end="")
    print()