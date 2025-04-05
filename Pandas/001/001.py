import pandas as pd
import numpy as np

csv = pd.read_csv("./StudentsPerformance.csv")

# print(csv.head())
# print(csv.shape)
# print(csv.info())
# print(csv.tail())
# print(csv.describe(include='all'))
print(csv.fillna('null'))

# exercicio do gpt

df = pd.read_csv('funcionarios.csv')
exibirPrimeirasLinhas = df.shape
remotos = df.loc['remoto']
salarioCincoMil = df[df['salario'] > 5000]
mediaSalarial = df.groupby('departamento').mean()
tempoEmpresa = df.sort_values('tempo_empres')
renomear = df.rename(columns={'tempo_empresa': "anos_na_empresa"})
