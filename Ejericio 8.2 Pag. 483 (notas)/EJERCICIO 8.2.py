import tkinter as tk
from tkinter import messagebox
import math

class Notas:
    """
    Clase que define una lista de notas numéricas y realiza cálculos estadísticos.
    """
    def __init__(self, lista_notas):
        self.lista_notas = lista_notas

    def calcular_promedio(self):
        suma = sum(self.lista_notas)
        return suma / len(self.lista_notas)

    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = sum(math.pow(nota - prom, 2) for nota in self.lista_notas)
        return math.sqrt(suma / len(self.lista_notas))

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)


class VentanaPrincipal:
    """
    Clase que define la interfaz gráfica para ingresar y calcular operaciones sobre notas.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("280x380")
        self.root.resizable(False, False)
        
        self.inicio()

    def inicio(self):
        # Etiquetas y campos de texto para las notas
        tk.Label(self.root, text="Nota 1:").place(x=20, y=20, width=80, height=23)
        self.campo_nota1 = tk.Entry(self.root)
        self.campo_nota1.place(x=105, y=20, width=135, height=23)

        tk.Label(self.root, text="Nota 2:").place(x=20, y=50, width=80, height=23)
        self.campo_nota2 = tk.Entry(self.root)
        self.campo_nota2.place(x=105, y=50, width=135, height=23)

        tk.Label(self.root, text="Nota 3:").place(x=20, y=80, width=80, height=23)
        self.campo_nota3 = tk.Entry(self.root)
        self.campo_nota3.place(x=105, y=80, width=135, height=23)

        tk.Label(self.root, text="Nota 4:").place(x=20, y=110, width=80, height=23)
        self.campo_nota4 = tk.Entry(self.root)
        self.campo_nota4.place(x=105, y=110, width=135, height=23)

        tk.Label(self.root, text="Nota 5:").place(x=20, y=140, width=80, height=23)
        self.campo_nota5 = tk.Entry(self.root)
        self.campo_nota5.place(x=105, y=140, width=135, height=23)

        # Botones
        self.btn_calcular = tk.Button(self.root, text="Calcular", command=self.calcular_accion)
        self.btn_calcular.place(x=20, y=170, width=100, height=23)

        self.btn_limpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar_accion)
        self.btn_limpiar.place(x=125, y=170, width=80, height=23)

        # Etiquetas de resultados
        self.lbl_promedio = tk.Label(self.root, text="Promedio = ", anchor="w")
        self.lbl_promedio.place(x=20, y=210, width=240, height=23)

        self.lbl_desviacion = tk.Label(self.root, text="Desviación = ", anchor="w")
        self.lbl_desviacion.place(x=20, y=240, width=240, height=23)

        self.lbl_mayor = tk.Label(self.root, text="Nota mayor = ", anchor="w")
        self.lbl_mayor.place(x=20, y=270, width=240, height=23)

        self.lbl_menor = tk.Label(self.root, text="Nota menor = ", anchor="w")
        self.lbl_menor.place(x=20, y=300, width=240, height=23)

    def calcular_accion(self):
        # Obtener los textos de los campos
        textos_notas = [
            self.campo_nota1.get(),
            self.campo_nota2.get(),
            self.campo_nota3.get(),
            self.campo_nota4.get(),
            self.campo_nota5.get()
        ]

        # Ejercicio propuesto 2: Validar que ninguna nota esté vacía
        for texto in textos_notas:
            if texto.strip() == "":
                messagebox.showwarning("Alerta", "Es obligatorio ingresar las cinco notas. Por favor llene todos los campos.")
                return

        # Ejercicio propuesto 1: Validar que los datos ingresados sean numéricos
        try:
            valores_notas = [float(texto) for texto in textos_notas]
        except ValueError:
            messagebox.showerror("Error de formato", "Se han ingresado datos que no son numéricos. Por favor ingrese solo números.")
            return

        # Si todo es correcto, se procede a calcular
        notas = Notas(valores_notas)

        promedio = notas.calcular_promedio()
        desviacion = notas.calcular_desviacion()
        mayor = notas.calcular_mayor()
        menor = notas.calcular_menor()

        # Actualizar las etiquetas con los resultados formateados a 2 decimales
        self.lbl_promedio.config(text=f"Promedio = {promedio:.2f}")
        self.lbl_desviacion.config(text=f"Desviación estándar = {desviacion:.2f}")
        self.lbl_mayor.config(text=f"Valor mayor = {mayor:.2f}")
        self.lbl_menor.config(text=f"Valor menor = {menor:.2f}")

    def limpiar_accion(self):
        # Limpiar los campos de texto
        self.campo_nota1.delete(0, tk.END)
        self.campo_nota2.delete(0, tk.END)
        self.campo_nota3.delete(0, tk.END)
        self.campo_nota4.delete(0, tk.END)
        self.campo_nota5.delete(0, tk.END)

        # Restablecer etiquetas
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")


if __name__ == "__main__":
    # Clase Principal: Punto de entrada al programa
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
