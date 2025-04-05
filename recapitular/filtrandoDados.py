import pandas as pd

dados = {
    "nome" : ["Ryan", "Cauã", "Iago", "Clauz"],
    "idade" : [10, 20, 30, 10]
}

df = pd.DataFrame(dados)

maior = df[df["idade"] >= 18]

print(f"maiores de idade: {maior}")