from tkinter import messagebox
import tkinter as tk

convert_ = 517.47

def close_window():
    if messagebox.askokcancel("¿salir?","¿Está seguro de que desea salir?"):
        window.destroy()


def clear_window():
    entry_usd.delete(0, tk.END)
    result.config(text="")

def convert():
    try:
        USD = float(entry_usd.get())
        CRC = USD * convert_
        result.config(text=f"{USD} USD = {CRC:.1f} CRC :) ")
    except ValueError:
        messagebox.showerror(":(","ingrese un número válido.")


window = tk.Tk()
window.title("convertidor de USD a CRC")
window.geometry("600x400")
window.protocol("WM_DELETE_WINDOW", close_window)

USD_label = tk.Label(window, text="ingrese el monto en dlares:")
USD_label.grid(row=0, column=0, padx=10, pady=10)
entry_usd = tk.Entry(window)
entry_usd.grid(row=0, column=1, padx=10, pady=10)

convert_bottom = tk.Button(window, text="Convertir a CRC", command=convert)
convert_bottom.grid(row=1, column=0, padx=10, pady=10)

clear_windo_bottom = tk.Button(window, text="Limpiar ventana", command=clear_window)
clear_windo_bottom.grid(row=1, column=1, padx=10, pady=10)

result = tk.Label(window, text="")
result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
