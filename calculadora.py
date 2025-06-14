import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Cambiar icono de la aplicación
ruta_icono = 'C:/Users/Simon/Desktop/python_aplicado/calculadora/calculadora.ico'
ventana.iconbitmap(ruta_icono)

# Variable para almacenar la expresión matematica
expresion = ""

# Variable para almacenar el estado del visor
resultado_mostrado = False

# Funcion para actualizar la expresion en el cuadro de texto
def pulsar_tecla(tecla):
    global expresion, resultado_mostrado

    # Evaluar si ya se ha calculado y mostrado un resultado
    if resultado_mostrado:
        # Evaluar si se presionó un numero o ".", reiniciar el visor
        if tecla.isdigit() or tecla == '.':
            expresion = str(tecla)
        else:
            expresion += str(tecla)
        resultado_mostrado = False
    else:
        expresion += str(tecla)
    visor_texto.set(expresion)

# Funcion para limpiar la entrada
def limpiar():
    global resultado_mostrado, expresion

    expresion = ""
    visor_texto.set(expresion)
    resultado_mostrado = False

# Funcion para evaluar la expresion y mostrar el resultado
def evaluar():
    global resultado_mostrado, expresion

    try:
        resultado = eval(expresion)
        # verificar si el resultado es un numero entero
        if resultado == int(resultado):
            resultado = int(resultado)
        visor_texto.set(str(resultado))
        expresion = str(resultado)
        resultado_mostrado = True
    except:
        visor_texto.set('Error')
        expresion = ""
        resultado_mostrado = False

# Configurar tamaño de las columnas y filas
for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(4):
    ventana.grid_columnconfigure(i, weight=1)

# cuadro de texto para mostrar las expresiones y resultado
visor_texto = tk.StringVar()
visor = tk.Entry(ventana,
                 textvariable=visor_texto,
                 font=('Helvetica', 32, 'bold'),
                 bd=10,
                 insertwidth=4,
                 width=14,
                 borderwidth=2,
                 justify='right',
                 relief='sunken',
                 bg='#0F1419',
                 fg='#E8F4FD'
                 )
visor.grid(row=0,
           column=0,
           columnspan=4,
           sticky='ew',
           padx=10,
           pady=10
           )

# Botones
botones = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,0),('.',4,1),('C',4,2),('+',4,3),
]

# Colores
color_fondo_numero = "#1E3A5F"           # Azul marino profundo para números
color_fondo_operacion = "#2E5984"        # Azul medio para operaciones (+, -, *, /)
color_fondo_especial = "#D63384"         # Rosa vibrante para especiales (C, CE, ±)
color_fondo_calcular = "#20C997"         # Turquesa brillante para igual (=) - ÚNICO
color_fondo_presionado = "#0F1419"       # Azul muy oscuro para presionado
color_fondo_calcular_presionado = "#17A085"  # Turquesa oscuro para igual presionado
color_texto_numero = "#E8F4FD"           # Azul muy claro para números
color_texto_especial = "#FFFFFF"         # Blanco puro para especiales


# Crear y posicionar los botones excepto "="
for (texto, fila, columna) in botones:
    if texto in ['/','*','-','+']:
        comando = lambda X=texto: pulsar_tecla(X)
        color_fondo = color_fondo_operacion
        color_texto = color_texto_especial

    elif texto == 'C':
        comando = limpiar
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial

    elif texto == '.':
        comando = lambda X=texto: pulsar_tecla(X)
        color_fondo = color_fondo_especial
        color_texto = color_texto_especial

    else:
        comando = lambda X=texto: pulsar_tecla(X)
        color_fondo = color_fondo_numero
        color_texto = color_texto_numero

    tk.Button(ventana,
              text=texto,
              padx=20,
              pady=20,
              font=('Helvetica', 20, 'bold'),
              command=comando,
              bd=1,
              relief='raised',
              bg=color_fondo,
              fg=color_texto,
              activeforeground=color_texto_especial,
              activebackground=color_fondo_presionado
               ).grid(row=fila,
                      column=columna,
                      sticky='nsew',
                      padx=2,
                      pady=2)

# Botón igual '='
tk.Button(ventana,
          text='=',
          padx=20,
          pady=20,
          font=('Helvetica', 40, 'bold'),
          command=evaluar,
          bd=1,
          relief='raised',
          bg=color_fondo_calcular,
          fg=color_texto_especial,
          activeforeground=color_texto_especial,
          activebackground=color_fondo_calcular_presionado
          ).grid(row=5,
                 column=0,
                 columnspan=4,
                 sticky='ew',
                 padx=2,
                 pady=2)

# Ejecuttar la aplicacion
ventana.mainloop()
