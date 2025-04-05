import tkinter as tk
from tkinter import messagebox

def calcular():
 try:
    expressao = entrada.get()
    resultado = eval(expressao)
    resultadoLabel.config(text=f"Resultado: {resultado}")
    
 except Exception as e:
   messagebox.showerror("Erro", "Expressão invalida")

calculadora = tk.Tk()
calculadora.title("Calculadora DInâmica")
calculadora.geometry("400x300")

instrucao = tk.Label(calculadora, text="Digite sua expressão matemática", font=("Arial", 15))
instrucao.pack(pady=10)

entrada = tk.Entry(calculadora, width=40, font=("Arial", 15))
entrada.pack(pady=10)
calculadora.mainloop()
