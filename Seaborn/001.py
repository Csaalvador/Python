import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style='darkgrid')

dados = sns.load_dataset('tips')
colunasRenomeadas = dados.rename(columns={
    'total_bill' : 'total da conta',
    'tip' : 'Gorjeta',
    'sex' : 'sexo',
    'smoker' : 'Fumante',
    'day' : 'Dia',
    'time': 'Tempo',
    'size': 'Quantidade'
})

# Cria o gráfico de regressão
sns.barplot(x='total da conta', y='Gorjeta', data=colunasRenomeadas, hue='sexo')

# Exibe o gráfico
plt.show()

