import tkinter as tk
from tkinter import *

#Variables que contienen el diccionario de encriptación
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabetoMayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
longitudAlfabeto = len(alfabeto)

#funcion para convertir texto a ascii
def textoAscii(texto):
    return ' '.join(list(map(str,map(ord, texto))))

#funcion para convertir texto a binario
def textoBinario(texto):
    return ' '.join(format(ord(c), 'b') for c in texto)

#funcion para convertir texto a hexadecimal   
def textoHexadecimal(texto):
    texto = texto.encode('utf-8')
    return texto.hex()

#funcion para encriptar en método Cesar
def desencriptar(mensaje, llave):
    textoDesencriptado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            textoDesencriptado += letra
            continue
        valor_letra = ord(letra)
        alfabeto_a_usar = alfabeto
        limite = 97
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabetoMayusculas
        posicion = (valor_letra - limite - llave) % longitudAlfabeto
        textoDesencriptado += alfabeto_a_usar[posicion]

    #Se asignan los resultados
    resultadoASCII.set(textoAscii(textoDesencriptado))
    resultadoBinario.set(textoBinario(textoDesencriptado))
    resultadoHexa.set(textoHexadecimal(textoDesencriptado))
    resultadoChar.set(textoDesencriptado)

#funcion para encriptar en método Cesar
def encriptar(mensaje, llave):
    textoEncriptado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            textoEncriptado += letra
            continue
        valorLetra = ord(letra)
        alfabetoAUsar = alfabeto
        limite = 97
        if letra.isupper():
            limite = 65
            alfabetoAUsar = alfabetoMayusculas
        posicion = (valorLetra - limite + llave) % longitudAlfabeto
        textoEncriptado += alfabetoAUsar[posicion]
    resultadoASCII.set(textoAscii(textoEncriptado))
    resultadoBinario.set(textoBinario(textoEncriptado))
    resultadoHexa.set(textoHexadecimal(textoEncriptado))
    resultadoChar.set(textoEncriptado)

#Función de asignación de opción, llamada desde el botón "encriptar o desencriptar"
def ejecutarOpcion(opcion, mensaje, llave):
    if opcion == "Encriptar":
        encriptar(mensaje, llave)
    else:
        desencriptar(mensaje, llave)

#funcion para crear ventana de encriptar/desencriptar
def ventanaMensaje(opcion):
    #Se crea la ventana de ingreso de información
    ventanaMensaje = Toplevel(ventana)
    ventanaMensaje.title(f"Guia 2 - {opcion}")
    ventanaMensaje.geometry("500x450")
    ventanaMensaje.resizable(0,0)
    ventanaMensaje.protocol("WM_DELETE_WINDOW", disable_event)
    ventanaMensaje.focus_set()

    #Cajas de texto para ingreso de datos
    Label(ventanaMensaje, text="Ingresa el mensaje:").place(x=50, y=50)
    Label(ventanaMensaje, text="Ingresa la llave:").place(x=50, y=100)
    mensaje = Entry(ventanaMensaje, width = 50)
    mensaje.place(x=175, y=50)
    llave = Entry(ventanaMensaje, width = 50, validate="key", validatecommand=(validation, "%S"))
    llave.place(x=175, y=100)
    Button(ventanaMensaje, text = opcion, width = 10, command= lambda: ejecutarOpcion(opcion, mensaje.get(), int(llave.get()))).place(x=400, y=150)

    #Cajas de texto de Resultados
    Label(ventanaMensaje, text="ASCII:").place(x=50, y=200)
    Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoASCII).place(x=175, y=200)

    Label(ventanaMensaje, text="Binario:").place(x=50, y=250)
    Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoBinario).place(x=175, y=250)    

    Label(ventanaMensaje, text="Hexadecimal:").place(x=50, y=300)
    Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoHexa).place(x=175, y=300)

    Label(ventanaMensaje, text="Char:").place(x=50, y=350)
    Entry(ventanaMensaje, width = 50, state="readonly", textvariable=resultadoChar).place(x=175, y=350)
    
    #Botón Salir
    Button(ventanaMensaje, text = "Salir", width = 10, command= lambda: salir(ventanaMensaje)).place(x=400, y=400)
    ventana.withdraw()

#Método para cerrar las ventanas
def salir(vModal):
    resultadoASCII.set("")
    resultadoBinario.set("")
    resultadoHexa.set("")
    resultadoChar.set("")
    vModal.withdraw()
    ventana.deiconify()

#Método para evitar que cierren la ventana
#por otra forma que no sea el botón
def disable_event():
    pass

#Método que valida que no permita letras
def only_numbers(char):
    return char.isdigit()

#ventana para el menu
ventana = Tk()
ventana.title("Guia 2 - Arquitectura")
ventana.geometry("350x100")
ventana.resizable(0,0)
cabecera = Label(ventana, text = "Método César").pack()

#Se registra la instancia de llamado de método de validación de solo números
validation = ventana.register(only_numbers)

#variables que contienen los resultados en cada calculo.
resultadoASCII = tk.StringVar()
resultadoBinario = tk.StringVar()
resultadoHexa = tk.StringVar()
resultadoChar = tk.StringVar()

#creacion de botones del menu
opcionEncriptar = Button(ventana, text="Encriptar Mensaje", command= lambda: ventanaMensaje("Encriptar")).place(x = 50, y = 50)
opcionDesencriptar = Button(ventana, text="Desencriptar Mensaje", command= lambda: ventanaMensaje("Desencriptar")).place(x = 200, y = 50)

ventana.mainloop()