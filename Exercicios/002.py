nota1, nota2, nota3 = map(float, input("Digite as notas: ").split())

def calcularMedia(x, y, z):
    result = (x + y + z)/3
    return result

media = calcularMedia(nota1, nota2, nota3)
print(media)