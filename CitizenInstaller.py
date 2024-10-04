import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame  # Importar pygame

# Inicializar pygame y la mezcla de audio
pygame.mixer.init()

# Función para reproducir música de fondo
def reproducir_musica():
    pygame.mixer.music.load("C:/Users/lekim/Desktop/CITIZENINSTALLLER/cositas.mp3")
    pygame.mixer.music.play(-1)  # Reproducir en bucle indefinido

# Función para elegir la ruta de instalación de FiveM
def seleccionar_ruta_fivem():
    ruta = filedialog.askdirectory()
    ruta_fivem_entry.delete(0, tk.END)
    ruta_fivem_entry.insert(0, ruta)

# Función para elegir la ruta de los citizens (PvP/Realista)
def seleccionar_ruta_citizens():
    ruta = filedialog.askdirectory()
    ruta_citizens_entry.delete(0, tk.END)
    ruta_citizens_entry.insert(0, ruta)

# Función para realizar la instalación
def instalar():
    ruta_fivem = ruta_fivem_entry.get()
    ruta_citizens = ruta_citizens_entry.get()
    
    if not os.path.exists(ruta_fivem) or not os.path.exists(ruta_citizens):
        messagebox.showerror("Error", "Una o ambas rutas no son válidas")
        return

    try:
        for folder in ["citizen", "mods", "plugins"]:
            folder_path = os.path.join(ruta_fivem, folder)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
    except Exception as e:
        messagebox.showerror("Error", f"Error al borrar carpetas: {e}")
        return

    if pvp_var.get() == 1:
        instalar_carpetas(ruta_fivem, os.path.join(ruta_citizens, "pvp"))
    else:
        instalar_carpetas(ruta_fivem, os.path.join(ruta_citizens, "realism"))
    
    messagebox.showinfo("Éxito", "Instalación completada.")

# Función para copiar las carpetas
def instalar_carpetas(destino, source_folder):
    try:
        for folder in ["citizen", "mods", "plugins"]:
            shutil.copytree(os.path.join(source_folder, folder), os.path.join(destino, folder))
    except Exception as e:
        messagebox.showerror("Error", f"Error al copiar carpetas: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Citizen Installer")

# Eliminar el ícono de la ventana
ventana.iconbitmap('')  # Esto debería quitar el logo de la ventana
ventana.config(bg="#0a0a0a")  # Color de fondo
ventana.geometry("500x250")   # Tamaño más compacto

# Título y creador
titulo = tk.Label(ventana, text="Citizen Installer", font=("Helvetica", 16, "bold"), bg="#0a0a0a", fg="white")
titulo.grid(row=0, column=0, columnspan=3, pady=10)
creador = tk.Label(ventana, text="Created by [El puto lekim]", font=("Helvetica", 10), bg="#0a0a0a", fg="white")
creador.grid(row=1, column=0, columnspan=3)

# Ruta de instalación de FiveM
tk.Label(ventana, text="Ruta de instalación de FiveM:", bg="#0a0a0a", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="e")
ruta_fivem_entry = tk.Entry(ventana, width=30)
ruta_fivem_entry.grid(row=2, column=1, pady=5)
tk.Button(ventana, text="Seleccionar ruta", command=seleccionar_ruta_fivem, bg="#940606", fg="white").grid(row=2, column=2, padx=5, pady=5)

# Ruta de citizens PvP/Realista
tk.Label(ventana, text="Ruta de carpetas PvP/Realista:", bg="#0a0a0a", fg="white").grid(row=3, column=0, padx=5, pady=5, sticky="e")
ruta_citizens_entry = tk.Entry(ventana, width=30)
ruta_citizens_entry.grid(row=3, column=1, pady=5)
tk.Button(ventana, text="Seleccionar ruta", command=seleccionar_ruta_citizens, bg="#940606", fg="white").grid(row=3, column=2, padx=5, pady=5)

# Opciones de PvP y Realista con el botón de instalar a la derecha
pvp_var = tk.IntVar()
tk.Radiobutton(ventana, text="PvP", variable=pvp_var, value=1, bg="#0a0a0a", fg="white", selectcolor="#1ABC9C").grid(row=4, column=0, sticky="e", padx=10, pady=5)
tk.Radiobutton(ventana, text="Realista", variable=pvp_var, value=2, bg="#0a0a0a", fg="white", selectcolor="#1ABC9C").grid(row=4, column=1, sticky="w", padx=10, pady=5)

# Botón de instalación
tk.Button(ventana, text="Instalar", command=instalar, bg="#940683", fg="white", font=("Helvetica", 10, "bold")).grid(row=4, column=2, padx=5, pady=5)

# Reproducir música al iniciar la aplicación
reproducir_musica()

ventana.mainloop()
