import pandas as pd

dias_semana = pd.Dias(["Segunda", "Terça", "Quarta", "Quinta", "Sexta"], colunms=["Dias"])

dias_semana["Dias"] = dias_semana["Dias"].astype(str)

print(dias_semana)