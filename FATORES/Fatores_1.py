import pandas as pd 

# Criando uma Series do Pandas com os dados
fatorial_1 = pd.Series(["vermelho", "Azul", "Verde"])

# Convertendo a Series para o tipo de dado categórico
fatorial_1 = fatorial_1.astype('category')

print(fatorial_1)