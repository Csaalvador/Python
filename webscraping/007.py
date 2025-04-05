import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('funcionarios.csv')
primeirosCinco = df.head()
linhasColunas = df.shape
nomeColunas = df.columns
tiposdeDados = df.dtypes
valoresNulos = df.isnull().sum()
salariosAcima = df[df['salario'] > 5000]
ti = df[df['departamento'] == 'TI']
funcMaisCincoAnos = df[df['tempo_empresa'] > 3]
remotos = df[df['remoto'] == 'Sim']
media = df['salario'].mean()
mediana = df['salario'].median()
valorMin = df[df['salario'] == df['salario'].min()]
valorMax = df[df['salario'] == df['salario'].max()]
funcionarios = df['nome'].count()
tiposDeContratos = df['departamento'].value_counts()

# Definindo as condições para as faixas salariais
condicoes = [
    (df['salario'] > 5000),  # Faixa Alta
    (df['salario'] > 3000) & (df['salario'] <= 5000),  # Faixa Média
    (df['salario'] <= 3000)  # Faixa Baixa
]

faixas = ['Alta', 'Média', 'Baixa']

df['faixa_salarial'] = np.select(condicoes, faixas, default='Indefinido')

mediaSalarial = df.groupby('departamento')['salario'].mean()
maiorQntdPessoas = df['departamento'].value_counts().idxmax()

tempoMedioDepartamento = df.groupby('departamento')['tempo_empresa'].mean()

pessoasPorDepartamento = df[df['remoto'] == 'Sim'].groupby('departamento')['remoto'].count()

# print(pessoasPorDepartamento)

graficoDepartamento = df.groupby('departamento')['nome'].count()

# graficoDepartamento.plot(kind='bar')
distribuicaodeSalarios = df['salario']
distribuicaodeSalarios.hist()
plt.show()

# print(distribuicaodeSalarios)