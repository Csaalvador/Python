horario = int(input(""))

hr = horario//3600
horario = horario - (hr * 3600)

min = horario//60
horario = horario - (min * 60)

print(f"{hr}:{min}:{horario}")