import random

vetor_og= [random.randint (1,100) for _ in range (20)]

vetor_in= vetor_og[::-1]

print("O maior valor no vetor é:",vetor_og)
print("O menor valor no vetor é:", vetor_in)