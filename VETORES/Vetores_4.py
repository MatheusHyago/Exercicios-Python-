import random

vetor = [random.randint (1,1000) for _ in range (50)]

maior_valor = max (vetor)

menor_valor = min (vetor)

print("O maior valor no vetor é:", maior_valor)
print("O menor valor no vetor é:", menor_valor)