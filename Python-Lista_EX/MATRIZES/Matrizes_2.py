matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0], [0,0,0,0]]
for l  in range (0,4):
    for c in range (0,4):
         matriz[l][c] = int(input(f"Digite os valores: "))

print('-='*40)
for l in range (0,4):
     for c in range (0,4):
          print(f"[{matriz[l][c]:^5}]", end="")
     print()