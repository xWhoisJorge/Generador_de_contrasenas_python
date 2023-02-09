import tkinter as tk
import random
import string

def generar_contraseña():
    contraseña = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    lista_contraseñas.insert(tk.END, contraseña)

def guardar_contraseñas():
    with open("contraseñas.txt", "w") as archivo:
        contraseñas = [lista_contraseñas.get(idx) for idx in range(lista_contraseñas.size())]
        archivo.write("\n".join(contraseñas))

root = tk.Tk()
root.title("Generador de contraseñas")
root.config(bg='#333333')
root.geometry("400x400")

etiqueta = tk.Label(root, text="Contraseñas generadas:", bg='#333333', fg='white')
etiqueta.pack(pady=10)

lista_contraseñas = tk.Listbox(root, height=5, width=30, bg='#444444', fg='white')
lista_contraseñas.pack()

botón_generar = tk.Button(root, text="Generar", command=generar_contraseña, bg='#555555', fg='white')
botón_generar.pack(pady=10)

botón_guardar = tk.Button(root, text="Guardar", command=guardar_contraseñas, bg='#555555', fg='white')
botón_guardar.pack(pady=10)

root.mainloop()
