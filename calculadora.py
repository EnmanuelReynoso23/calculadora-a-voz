import tkinter as tk
import speech_recognition as sr


def calcular():
    # Obtener la operación ingresada por el usuario
    operacion = resultado.get()

    try:
        # Evaluar la operación y realizar el cálculo
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, eval(operacion))
    except:
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, "Error")

def capturar_operacion():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di los números:")
        audio = r.listen(source)
    
    try:
        numeros = r.recognize_google(audio, language="es-ES")
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, numeros)
    except sr.UnknownValueError:
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, "Syntax Error")
    except sr.RequestError as e:
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, "Error al procesar la solicitud")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
def calcular():
    # Obtener la operación ingresada por el usuario
    operacion = resultado.get()

    try:
        # Evaluar la operación y realizar el cálculo de audio del
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, eval(operacion))
    except:
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, "Error")

def capturar_operacion():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di los números:")
        audio = r.listen(source, timeout=15)  # Set timeout to 15 seconds
    
    try:
        numeros = r.recognize_google(audio, language="es-ES")
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, numeros)
    except sr.UnknownValueError:
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, "Syntax Error")
    except sr.RequestError as e:
        resultado.delete(0, tk.END)
        resultado.insert(tk.END, "Error al procesar la solicitud")

# Rest of the code remains the same

# Agregar un campo de texto para mostrar los resultados
resultado = tk.Entry(ventana)
resultado.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Agregar un botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular, bg="green", fg="white", height=4, width=20)
boton_calcular.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Agregar un botón para capturar la operación desde el micrófono
boton_mic = tk.Button(ventana, text="Capturar Operación", command=capturar_operacion, bg="red", fg="white", height=4, width=20)
boton_mic.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Agregar botones para las operaciones
boton_suma = tk.Button(ventana, text="+", command=lambda: resultado.insert(tk.END, "+"), bg="yellow", fg="black", height=4, width= 10)
boton_resta = tk.Button(ventana, text="-", command=lambda: resultado.insert(tk.END, "-"), bg="yellow", fg="black", height=4, width=10)
boton_multiplicacion = tk.Button(ventana, text="*", command=lambda: resultado.insert(tk.END, "*"), bg="yellow", fg="black", height=4, width=10)
boton_division = tk.Button(ventana, text="/", command=lambda: resultado.insert(tk.END, "/"), bg="yellow", fg="black", height=4, width=10)

# Configurar tamaño y posición de los botones
boton_suma.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
boton_resta.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")
boton_multiplicacion.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")
boton_division.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")

# Configurar el espaciado uniforme de las columnas y filas
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_columnconfigure(2, weight=1)
ventana.grid_columnconfigure(3, weight=1)
ventana.grid_rowconfigure(4, weight=1)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
