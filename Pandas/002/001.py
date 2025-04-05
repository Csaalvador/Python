import pandas as pd

# ✅ Tarefas que você precisa resolver com pandas:
# Ler o arquivo CSV com pandas.


# Salvar o novo DataFrame em outro CSV chamado funcionarios_limpo.csv.

df = pd.read_csv("funcionarios.csv") 
PrimeirosLinha = df.head()
remotos = df[df['remoto'] == 'Sim']
salariosAltos = df[df['salario'] > 4000]
mediaSalarial = df.groupby('departamento')['salario'].mean()
tempoEmpresa = df.sort_values('tempo_empresa', ascending=False)
renomear = df.rename(columns={'tempo_empresa': "anos_na_empresa"})
nulos = df.isnull().sum()

df.to_csv('funcionarios_limpo.csv', index=False)

print(nulos)