import tkinter as tk
from tkinter import messagebox


def obtener_numeros():
    try:
        n1 = float(entrada_num1.get().replace(",", "."))
        n2 = float(entrada_num2.get().replace(",", "."))
        return n1, n2
    except ValueError:
        messagebox.showerror("Entrada no válida", "Por favor, escribe números válidos.")
        return None, None


def calcular(operacion):
    n1, n2 = obtener_numeros()
    if n1 is None or n2 is None:
        return

    if operacion == "sumar":
        resultado = n1 + n2
        simbolo = "+"
    elif operacion == "restar":
        resultado = n1 - n2
        simbolo = "-"
    elif operacion == "multiplicar":
        resultado = n1 * n2
        simbolo = "×"
    elif operacion == "dividir":
        if n2 == 0:
            messagebox.showerror("Error matemático", "No se puede dividir entre cero.")
            return
        resultado = n1 / n2
        simbolo = "÷"

    etiqueta_resultado.config(text=f"{n1} {simbolo} {n2} = {resultado}")


def limpiar():
    entrada_num1.delete(0, tk.END)
    entrada_num2.delete(0, tk.END)
    etiqueta_resultado.config(text="Resultado: ---")


ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("360x280")
ventana.resizable(False, False)

tk.Label(ventana, text="Calculadora", font=("Segoe UI", 16, "bold")).pack(pady=(14, 8))

marco_entradas = tk.Frame(ventana)
marco_entradas.pack(pady=4)

tk.Label(marco_entradas, text="Primer número:", font=("Segoe UI", 10)).grid(row=0, column=0, padx=6, pady=6, sticky="e")
entrada_num1 = tk.Entry(marco_entradas, font=("Segoe UI", 11), width=16)
entrada_num1.grid(row=0, column=1, padx=6, pady=6)

tk.Label(marco_entradas, text="Segundo número:", font=("Segoe UI", 10)).grid(row=1, column=0, padx=6, pady=6, sticky="e")
entrada_num2 = tk.Entry(marco_entradas, font=("Segoe UI", 11), width=16)
entrada_num2.grid(row=1, column=1, padx=6, pady=6)

marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=10)

tk.Button(marco_botones, text="Sumar (+)", width=12, font=("Segoe UI", 10), command=lambda: calcular("sumar")).grid(row=0, column=0, padx=5, pady=4)
tk.Button(marco_botones, text="Restar (-)", width=12, font=("Segoe UI", 10), command=lambda: calcular("restar")).grid(row=0, column=1, padx=5, pady=4)
tk.Button(marco_botones, text="Multiplicar (×)", width=12, font=("Segoe UI", 10), command=lambda: calcular("multiplicar")).grid(row=1, column=0, padx=5, pady=4)
tk.Button(marco_botones, text="Dividir (÷)", width=12, font=("Segoe UI", 10), command=lambda: calcular("dividir")).grid(row=1, column=1, padx=5, pady=4)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ---", font=("Segoe UI", 12, "bold"))
etiqueta_resultado.pack(pady=(6, 4))

tk.Button(ventana, text="Limpiar", width=10, font=("Segoe UI", 9), command=limpiar).pack()

ventana.mainloop()
