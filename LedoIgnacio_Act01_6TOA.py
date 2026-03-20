
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- CREACIÓN DE LA VENTANA PRINCIPAL ---
# tk.Tk() es lo que "arranca" la interfaz gráfica
ventana = tk.Tk()
ventana.title("Menú Heladería")
# geometry define el tamaño de la ventana (ancho x alto)
ventana.geometry("500x750") 

color_fondo = "#FFE4E1"  
color_texto = "#8B4513"  

# configure(bg=...) le cambia el color de fondo a la ventana
ventana.configure(bg=color_fondo)

# tk.IntVar() es una variable especial de Tkinter. 
# Las variables normales de Python no funcionan bien para actualizar la pantalla, 
# por eso usamos IntVar para guardar números enteros (como la opción elegida).
opcion_t = tk.IntVar()


# --- FUNCIONES ---

def mostrar_sabores():
    # .get() lee el valor que tiene guardado la variable especial opcion_t
    if opcion_t.get() == 0:
        # messagebox.showinfo abre una ventanita emergente con un mensaje
        messagebox.showinfo("Error", "Por favor, elige un tamaño primero.")
        return
        
    # .pack() sirve para "pegar" o ubicar un elemento en la ventana, uno abajo del otro.
    sabores.pack(pady=10, padx=20, fill="both") 
    boton_final.pack(pady=15) 
    
    # .pack_forget() hace lo contrario: esconde el elemento de la pantalla.
    # Acá escondemos el botón "Elegir Sabores" porque ya lo apretaron.
    boton_siguiente.pack_forget()
  


def obtener_detalles_tamano(opcion):
    # Una función simple que devuelve (precio, cantidad_permitida, nombre)
    if opcion == 1: return (700, 1, "1 Bocha")
    if opcion == 2: return (1200, 2, "2 Bochas")
    if opcion == 3: return (1600, 3, "3 Bochas")
    if opcion == 4: return (2500, 1, "1/4 Kilo") 
    if opcion == 5: return (4500, 2, "1/2 Kilo") 
    if opcion == 6: return (8000, 3, "1 Kilo")   
    return (0, 0, "")


def terminar():
    # Volvemos a tu lista clásica para guardar los sabores
    saboras = []

    # Verificamos uno por uno. Si el Checkbutton está tildado, su valor es 1.
    if limonA.get() == 1: saboras.append("Limón")
    if frutillA.get() == 1: saboras.append("Frutilla")
    if ananaA.get() == 1: saboras.append("Ananá")
    if nranjaA.get() == 1: saboras.append("Naranja")
    if vainillA.get() == 1: saboras.append("Vainilla")
    if ddelecheA.get() == 1: saboras.append("Dulce de Leche")
    if tramntanA.get() == 1: saboras.append("Tramontana")

    seleccion = opcion_t.get()

    precio, max_sabores, nombre_tamano = obtener_detalles_tamano(seleccion)

    # Controles básicos antes de cobrar
    if len(saboras) > max_sabores:
        messagebox.showinfo("Ojo", f"Para '{nombre_tamano}' solo puedes elegir hasta {max_sabores} sabor(es).")
        return
        
    if len(saboras) == 0:
        messagebox.showinfo("Faltan sabores", "Debes elegir al menos un sabor.")
        return

    resumen_texto = f"Tamaño: {nombre_tamano}\nSabores: {', '.join(saboras)}\nTotal: ${precio}"

    # Guardamos en el archivo. 
    # La "a" significa "append" (agregar al final sin borrar lo anterior).
    try:
        with open("historial_ventas.txt", "a", encoding="utf-8") as archivo:
            ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            archivo.write(f"[{ahora}] {nombre_tamano} | Sabores: {', '.join(saboras)} | ${precio}\n")
    except Exception as e:
        print("Error al guardar:", e)

    messagebox.showinfo("Ticket de Compra", resumen_texto)
    limpiar_pedido()


def limpiar_pedido():
    # .set() sirve para cambiar el valor de la variable de Tkinter. 
    # Le ponemos 0 a todo para destildar las opciones.
    opcion_t.set(0)
    limonA.set(0); frutillA.set(0); ananaA.set(0); nranjaA.set(0)
    vainillA.set(0); ddelecheA.set(0); tramntanA.set(0)
    
    # Escondemos los sabores y el botón final, y volvemos a mostrar el botón de siguiente
    sabores.pack_forget()
    boton_final.pack_forget()
    boton_siguiente.pack(pady=15, ipadx=10, ipady=5)


def ver_historial():
    try:
        # La "r" significa "read" (modo lectura). Solo leemos el archivo.
        with open("historial_ventas.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            
        # tk.Toplevel() crea una ventana secundaria (hija de la principal).
        ventana_historial = tk.Toplevel(ventana)
        ventana_historial.title("Historial de Ventas")
        ventana_historial.geometry("450x450")
        
        # Le agrego el Scrollbar (barra lateral) que te faltaba para poder bajar
        scrollbar = tk.Scrollbar(ventana_historial)
        scrollbar.pack(side="right", fill="y") # Lo pego a la derecha

        # tk.Text() es una caja de texto grande multidínea.
        # yscrollcommand conecta la caja de texto con la barra lateral.
        cuadro_texto = tk.Text(ventana_historial, yscrollcommand=scrollbar.set)
        cuadro_texto.pack(expand=True, fill="both")
        
        # Le digo a la barra lateral que mueva el texto en el eje Y (vertical)
        scrollbar.config(command=cuadro_texto.yview)

        # tk.END indica que inserte el texto desde el principio hasta el final.
        cuadro_texto.insert(tk.END, contenido)
        # Lo pongo en 'disabled' para que el usuario no pueda borrar el texto sin querer
        cuadro_texto.config(state="disabled") 
        
    except FileNotFoundError:
        messagebox.showinfo("Aviso", "Aún no hay ventas registradas.")


# --- DISEÑO DE LA INTERFAZ ---

lbl_titulo = tk.Label(ventana, text="HELADERÍA 🍦 DULCE FRÍO 🍦", font=("Trebuchet MS", 22, "bold"), bg=color_fondo, fg=color_texto)
lbl_titulo.pack(pady=20) 

# LabelFrame es como un rectangulito con un título arriba para agrupar cosas
frame_tamanos = tk.LabelFrame(ventana, text=" 1. ELIGE EL TAMAÑO ", bg=color_fondo)
frame_tamanos.pack(pady=5, padx=20, fill="both")

# tk.Radiobutton son los circulitos de opción única (si elegís uno, se desmarca el otro)
tk.Radiobutton(frame_tamanos, text="1 Bocha - $700", variable=opcion_t, value=1, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="2 Bochas - $1200", variable=opcion_t, value=2, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="3 Bochas - $1600", variable=opcion_t, value=3, bg=color_fondo).pack(anchor="w")

tk.Radiobutton(frame_tamanos, text="1/4 Kilo - $2500", variable=opcion_t, value=4, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="1/2 Kilo - $4500", variable=opcion_t, value=5, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="1 Kilo - $8000", variable=opcion_t, value=6, bg=color_fondo).pack(anchor="w")

# tk.Button es un botón normal que ejecuta una función cuando le hacés clic (command=...)
boton_siguiente = tk.Button(ventana, text="Elegir Sabores", command=mostrar_sabores, bg="#FF4500", fg="white")
boton_siguiente.pack(pady=15)

sabores = tk.LabelFrame(ventana, text=" 2. ELIGE TUS SABORES ", bg=color_fondo)

limonA = tk.IntVar(); frutillA = tk.IntVar(); ananaA = tk.IntVar()
nranjaA = tk.IntVar(); vainillA = tk.IntVar(); ddelecheA = tk.IntVar()
tramntanA = tk.IntVar()


# tk.Checkbutton son los cuadraditos que podés tildar y destildar (múltiples opciones)
# Usamos .grid() acá porque nos permite acomodarlos como en una tabla (filas y columnas)
tk.Checkbutton(sabores, text="Limón", variable=limonA, bg=color_fondo).grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Frutilla", variable=frutillA, bg=color_fondo).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Ananá", variable=ananaA, bg=color_fondo).grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Naranja", variable=nranjaA, bg=color_fondo).grid(row=3, column=0, sticky="w", padx=10)

tk.Checkbutton(sabores, text="Vainilla", variable=vainillA, bg=color_fondo).grid(row=0, column=1, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Dulce de leche", variable=ddelecheA, bg=color_fondo).grid(row=1, column=1, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Tramontana", variable=tramntanA, bg=color_fondo).grid(row=2, column=1, sticky="w", padx=10)

boton_final = tk.Button(ventana, text="CONFIRMAR PEDIDO", command=terminar, bg="#32CD32", fg="white")

boton_historial = tk.Button(ventana, text="Ver Historial de Ventas", command=ver_historial, bg="#4682B4", fg="white")
boton_historial.pack(side="bottom", pady=15)

# mainloop() es lo que mantiene la ventana abierta esperando que hagamos clic en algo

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- CREACIÓN DE LA VENTANA PRINCIPAL ---
# tk.Tk() es lo que "arranca" la interfaz gráfica
ventana = tk.Tk()
ventana.title("Menú Heladería")
# geometry define el tamaño de la ventana (ancho x alto)
ventana.geometry("500x750") 

color_fondo = "#FFE4E1"  
color_texto = "#8B4513"  

# configure(bg=...) le cambia el color de fondo a la ventana
ventana.configure(bg=color_fondo)

# tk.IntVar() es una variable especial de Tkinter. 
# Las variables normales de Python no funcionan bien para actualizar la pantalla, 
# por eso usamos IntVar para guardar números enteros (como la opción elegida).
opcion_t = tk.IntVar()


# --- FUNCIONES ---

def mostrar_sabores():
    # .get() lee el valor que tiene guardado la variable especial opcion_t
    if opcion_t.get() == 0:
        # messagebox.showinfo abre una ventanita emergente con un mensaje
        messagebox.showinfo("Error", "Por favor, elige un tamaño primero.")
        return
        
    # .pack() sirve para "pegar" o ubicar un elemento en la ventana, uno abajo del otro.
    sabores.pack(pady=10, padx=20, fill="both") 
    boton_final.pack(pady=15) 
    
    # .pack_forget() hace lo contrario: esconde el elemento de la pantalla.
    # Acá escondemos el botón "Elegir Sabores" porque ya lo apretaron.
    boton_siguiente.pack_forget()


def obtener_detalles_tamano(opcion):
    # Una función simple que devuelve (precio, cantidad_permitida, nombre)
    if opcion == 1: return (700, 1, "1 Bocha")
    if opcion == 2: return (1200, 2, "2 Bochas")
    if opcion == 3: return (1600, 3, "3 Bochas")
    if opcion == 4: return (2500, 1, "1/4 Kilo") 
    if opcion == 5: return (4500, 2, "1/2 Kilo") 
    if opcion == 6: return (8000, 3, "1 Kilo")   
    return (0, 0, "")


def terminar():
    # Volvemos a tu lista clásica para guardar los sabores
    saboras = []

    # Verificamos uno por uno. Si el Checkbutton está tildado, su valor es 1.
    if limonA.get() == 1: saboras.append("Limón")
    if frutillA.get() == 1: saboras.append("Frutilla")
    if ananaA.get() == 1: saboras.append("Ananá")
    if nranjaA.get() == 1: saboras.append("Naranja")
    if vainillA.get() == 1: saboras.append("Vainilla")
    if ddelecheA.get() == 1: saboras.append("Dulce de Leche")
    if tramntanA.get() == 1: saboras.append("Tramontana")

    seleccion = opcion_t.get()

    precio, max_sabores, nombre_tamano = obtener_detalles_tamano(seleccion)

    # Controles básicos antes de cobrar
    if len(saboras) > max_sabores:
        messagebox.showinfo("Ojo", f"Para '{nombre_tamano}' solo puedes elegir hasta {max_sabores} sabor(es).")
        return
        
    if len(saboras) == 0:
        messagebox.showinfo("Faltan sabores", "Debes elegir al menos un sabor.")
        return

    resumen_texto = f"Tamaño: {nombre_tamano}\nSabores: {', '.join(saboras)}\nTotal: ${precio}"

    # Guardamos en el archivo. 
    # La "a" significa "append" (agregar al final sin borrar lo anterior).
    try:
        with open("historial_ventas.txt", "a", encoding="utf-8") as archivo:
            ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            archivo.write(f"[{ahora}] {nombre_tamano} | Sabores: {', '.join(saboras)} | ${precio}\n")
    except Exception as e:
        print("Error al guardar:", e)

    messagebox.showinfo("Ticket de Compra", resumen_texto)
    limpiar_pedido()


def limpiar_pedido():
    # .set() sirve para cambiar el valor de la variable de Tkinter. 
    # Le ponemos 0 a todo para destildar las opciones.
    opcion_t.set(0)
    limonA.set(0); frutillA.set(0); ananaA.set(0); nranjaA.set(0)
    vainillA.set(0); ddelecheA.set(0); tramntanA.set(0)
    
    # Escondemos los sabores y el botón final, y volvemos a mostrar el botón de siguiente
    sabores.pack_forget()
    boton_final.pack_forget()
    boton_siguiente.pack(pady=15, ipadx=10, ipady=5)


def ver_historial():
    try:
        # La "r" significa "read" (modo lectura). Solo leemos el archivo.
        with open("historial_ventas.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            
        # tk.Toplevel() crea una ventana secundaria (hija de la principal).
        ventana_historial = tk.Toplevel(ventana)
        ventana_historial.title("Historial de Ventas")
        ventana_historial.geometry("450x450")
        
        # Le agrego el Scrollbar (barra lateral) que te faltaba para poder bajar
        scrollbar = tk.Scrollbar(ventana_historial)
        scrollbar.pack(side="right", fill="y") # Lo pego a la derecha

        # tk.Text() es una caja de texto grande multidínea.
        # yscrollcommand conecta la caja de texto con la barra lateral.
        cuadro_texto = tk.Text(ventana_historial, yscrollcommand=scrollbar.set)
        cuadro_texto.pack(expand=True, fill="both")
        
        # Le digo a la barra lateral que mueva el texto en el eje Y (vertical)
        scrollbar.config(command=cuadro_texto.yview)

        # tk.END indica que inserte el texto desde el principio hasta el final.
        cuadro_texto.insert(tk.END, contenido)
        # Lo pongo en 'disabled' para que el usuario no pueda borrar el texto sin querer
        cuadro_texto.config(state="disabled") 
        
    except FileNotFoundError:
        messagebox.showinfo("Aviso", "Aún no hay ventas registradas.")


# --- DISEÑO DE LA INTERFAZ ---

lbl_titulo = tk.Label(ventana, text="HELADERÍA 🍦 DULCE FRÍO 🍦", font=("Trebuchet MS", 22, "bold"), bg=color_fondo, fg=color_texto)
lbl_titulo.pack(pady=20) 

# LabelFrame es como un rectangulito con un título arriba para agrupar cosas
frame_tamanos = tk.LabelFrame(ventana, text=" 1. ELIGE EL TAMAÑO ", bg=color_fondo)
frame_tamanos.pack(pady=5, padx=20, fill="both")

# tk.Radiobutton son los circulitos de opción única (si elegís uno, se desmarca el otro)
tk.Radiobutton(frame_tamanos, text="1 Bocha - $700", variable=opcion_t, value=1, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="2 Bochas - $1200", variable=opcion_t, value=2, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="3 Bochas - $1600", variable=opcion_t, value=3, bg=color_fondo).pack(anchor="w")

tk.Radiobutton(frame_tamanos, text="1/4 Kilo - $2500", variable=opcion_t, value=4, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="1/2 Kilo - $4500", variable=opcion_t, value=5, bg=color_fondo).pack(anchor="w")
tk.Radiobutton(frame_tamanos, text="1 Kilo - $8000", variable=opcion_t, value=6, bg=color_fondo).pack(anchor="w")

# tk.Button es un botón normal que ejecuta una función cuando le hacés clic (command=...)
boton_siguiente = tk.Button(ventana, text="Elegir Sabores", command=mostrar_sabores, bg="#FF4500", fg="white")
boton_siguiente.pack(pady=15)

sabores = tk.LabelFrame(ventana, text=" 2. ELIGE TUS SABORES ", bg=color_fondo)

limonA = tk.IntVar(); frutillA = tk.IntVar(); ananaA = tk.IntVar()
nranjaA = tk.IntVar(); vainillA = tk.IntVar(); ddelecheA = tk.IntVar()
tramntanA = tk.IntVar()

# tk.Checkbutton son los cuadraditos que podés tildar y destildar (múltiples opciones)
# Usamos .grid() acá porque nos permite acomodarlos como en una tabla (filas y columnas)
tk.Checkbutton(sabores, text="Limón", variable=limonA, bg=color_fondo).grid(row=0, column=0, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Frutilla", variable=frutillA, bg=color_fondo).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Ananá", variable=ananaA, bg=color_fondo).grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Naranja", variable=nranjaA, bg=color_fondo).grid(row=3, column=0, sticky="w", padx=10)

tk.Checkbutton(sabores, text="Vainilla", variable=vainillA, bg=color_fondo).grid(row=0, column=1, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Dulce de leche", variable=ddelecheA, bg=color_fondo).grid(row=1, column=1, sticky="w", padx=10)
tk.Checkbutton(sabores, text="Tramontana", variable=tramntanA, bg=color_fondo).grid(row=2, column=1, sticky="w", padx=10)

boton_final = tk.Button(ventana, text="CONFIRMAR PEDIDO", command=terminar, bg="#32CD32", fg="white")

boton_historial = tk.Button(ventana, text="Ver Historial de Ventas", command=ver_historial, bg="#4682B4", fg="white")
boton_historial.pack(side="bottom", pady=15)

# mainloop() es lo que mantiene la ventana abierta esperando que hagamos clic en algo

ventana.mainloop()