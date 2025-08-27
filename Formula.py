import tkinter as tk
from tkinter import PhotoImage
import os
import sys

#Ventana
root = tk.Tk()

''''Funciones'''''

#Carga y empaque las imagenes
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Aplica la formula segun los valores dados, revisando que no haya valores '0' e imprime los resultados
def FormulaResolvente(a, b, c):
    if a != 0 and b != 0 and c != 0:
        x1 = f'El primer(+) valor es {(-b + (b**2 - 4*a*c)**0.5) / (2*a)}'
        x2 = f'El segundo(-) valor es {(-b - (b**2 - 4*a*c)**0.5) / (2*a)}'
        imprimir_valor1 = tk.Label(root, text=x1, font=("Century Gothic", 10))
        imprimir_valor1.grid(row=6, column=0, sticky='w')
        imprimir_valor2 = tk.Label(root, text=x2, font=("Century Gothic", 10))
        imprimir_valor2.grid(row=7, column=0, sticky='w')
        boton2 = tk.Button(root, text="Limpiar", command=lambda: Limpiar(boton2, imprimir_valor1, imprimir_valor2),bg='red', fg='black')
        boton2.grid(row=8, column=1, columnspan=2, pady=20, padx=10)
    else:
        error = tk.Label(root, text="Error: No puede ser 0.", font=("Century Gothic", 10), fg="red")
        error.grid(row=5, column=0, columnspan=4, pady=5)
        boton2 = tk.Button(root, text="Limpiar", command=lambda: Limpiar(boton2, error, None),bg='red', fg='black')
        boton2.grid(row=8, column=1, columnspan=2, pady=20, padx=10)

#Limpia los resultados dados, tanto errores como valores
def Limpiar(boton, valor1, valor2):
    boton.destroy()
    if valor1: valor1.destroy()
    if valor2: valor2.destroy()

#Toma los datos que el usuario coloca en la interfaz. Revisa que los valores sean numericos.
def TomarDatos():
    try:
        termino_grado2 = eval(A.get())
        termino_grado1 = eval(B.get())
        termino_independiente = eval(C.get())
        FormulaResolvente(termino_grado2, termino_grado1, termino_independiente)
    except (ValueError, SyntaxError, NameError):
        error = tk.Label(root, text="Por favor, ingresa una expresión matemática válida.", font=("Century Gothic", 10), fg="red")
        error.grid(row=5, column=0, columnspan=4, pady=5)
        boton2 = tk.Button(root, text="Limpiar", command=lambda: Limpiar(boton2, error, None), bg='red', fg='black')
        boton2.grid(row=8, column=1, columnspan=2, pady=20, padx=10)
        
''''Interfaz Grafica'''''     
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.title("Formula Resolvente")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 800
window_height = 600

position_top = int((screen_height - window_height) / 2)
position_right = int((screen_width - window_width) / 2)

root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.resizable(False, False)

path_icon = resource_path('Resolvente\RinIcon.ico')
root.iconbitmap(path_icon)

path_fondo = resource_path('Resolvente\RinFondo.png')
Fondo = PhotoImage(file=path_fondo)
label_fondo = tk.Label(root, image=Fondo)
label_fondo.place(x=0, y=0, relheight=1, relwidth=1)

Titulo = tk.Label(root, text="Formula Resolvente", font=("Century Gothic", 20), bg='#F28500', fg='black')
Titulo.grid(row=0, column=0, columnspan=4, padx=30, pady=20, sticky='n')

formula = tk.Label(root, text="(-b + - (b**2 - 4*a*c)**0.5) / (2*a)", font=("Century Gothic", 15),bg='#F28500', fg='black')
formula.grid(row=1, column=0, columnspan=4, padx=30, pady=10, sticky='n')

InputA = tk.Label(root, text="Dime el termino de Grado 2(a):", font=("Century Gothic", 10),bg='#F28500', fg='black')
InputA.grid(row=2, column=0, padx=10, pady=10, sticky='w')
A = tk.Entry(root)
A.grid(row=2, column=1, padx=10, pady=10, sticky='w')

InputB = tk.Label(root, text="Dime el termino de Grado 1(b):", font=("Century Gothic", 10),bg='#F28500', fg='black')
InputB.grid(row=3, column=0, padx=10, pady=10, sticky='w')
B = tk.Entry(root)
B.grid(row=3, column=1, padx=10, pady=10, sticky='w')

InputC = tk.Label(root, text="Dime el termino Independiente(c):", font=("Century Gothic", 10),bg='#F28500', fg='black')
InputC.grid(row=4, column=0, padx=10, pady=10, sticky='w')
C = tk.Entry(root)
C.grid(row=4, column=1, padx=10, pady=10, sticky='w')

boton1 = tk.Button(root, text="Calcular", command=TomarDatos,bg='#F28500', fg='black')
boton1.grid(row=5, column=1, columnspan=2, pady=20, padx=10)

boton = tk.Button(root, text="Cerrar", command=root.destroy,bg='#F28500', fg='black')
boton.grid(row=9, column=1, columnspan=2, pady=20, padx=10)

aclaracion = tk.Label(root, text="PERMITIMOS NOTACION CIENTIFICA!\nEscribir las multiplicaciones con '*', \nlas potencias con '**', \nla division con '/' y \nla raiz como una potencia elevada a \n fraccion o decimal \n(ej: '1**1/2')",bg='#F28500', fg='black')
aclaracion.grid(row=2, column=3, rowspan=3, padx=20, pady=10, sticky='e')

root.mainloop()