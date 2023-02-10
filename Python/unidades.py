# Unidades de medida

"""
En primer lugar, hemos identificado que en muchos escenarios de la vida real los valores que manejamos no están expresados en las mismas unidades de medida. En este caso, el programa va a obtener los parámetros en las siguientes unidades:


- La posición inicial x0 en metros (m
).
- La velocidad inicial v0 en kilómetros por hora (km/h
).
- La aceleración a en metros sobre segundo al cuadrado (m/s2
).
- El tiempo t en segundos (s
).

Dado que la velocidad está dada en kilometros por hora, es necesario antes calcular algunas conversiones entre unidades de medida. Tenga en cuenta las siguientes equivalencias:

1 km = 1000 m <--> 1 m = 1/1000 km

1 h = 3600 s <--> 1 s = 1/3600 h

1 km / s = 1/3.6 m/s <--> 1 m/s = 3.6 km/s

------------------------------------------------------------------------------------------------------------------------------------

⌨️ Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

Su programa deberá recibir de la entrada 4 líneas con los valores de x0, v0, a y t respectivamente.


Línea 1: cadena de texto con la posición inicial x0 en m
.
Línea 2: cadena de texto con la velocidad inicial v0 en km/h
.
Línea 3: cadena de texto con la aceleración a en m/s2
.
Línea 4: cadena de texto con el tiempo t en s
.

Tenga en cuenta que cada una de estas líneas es obtenida como cadenas de texto con un formato que puede ser convertido a un valor decimal con la función float. No olvide realizar la conversión del tipo de dato en su programa.

--------------------------------------------------------------------------------------------------------------------------------------

🖥️ Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.


En este ejercicio el programa deberá imprimir exactamente 1 línea con la respuesta del ejercicio. Esta respuesta deberá tener este formato exacto:


'La posición final es de {x} m y la velocidad es de {v} km/h'


- {x} corresponde a la posición final calculada en metros (m
), que deberá ser presentada con un formato que muestre exactamente 2 dígitos decimales.
- {v} corresponde a la velocidad final calculada en kilómetros por hora (km/h
), que deberá ser presentada con un formato que muestre exactamente 3 dígitos decimales.

----------------------------------------------------------------------------------------------------------------------------------------

🧩 Ejemplos
Entrada Ejemplo 1

15
3.2
0
0
Salida Ejemplo 1

La posición final es de 15.00 m y la velocidad es de 3.200 km/h

Entrada Ejemplo 2

21.1
40
0.1
60
Salida Ejemplo 2

La posición final es de 867.77 m y la velocidad es de 61.600 km/h

Entrada Ejemplo 3

47
6
5e-2
147
Salida Ejemplo 3

La posición final es de 832.23 m y la velocidad es de 32.460 km/h
"""

##################################################
#### 💻 Tarea: Ejercicios de física (II)  💻 ####
##################################################

""" ## 👇 Escriba su código DEBAJO de esta línea 👇 ##


# 1) Obtener de la entrada del programa los parámetros iniciales.
# 2) Convertir cada valor de texto obtenido de la entrada en un valor numérico decimal.

x0 = float(input("Ingrese la posición inicial x0 en m: "))
v0 = float(input("Ingrese la velocidad inicial v0 en km/h: "))
a = float(input("Ingrese la aceleración a en m/s2: "))
t = float(input("Ingrese el tiempo t en s: "))

# 3) Realizar las operaciones matemáticas para las conversiones de unidad de medida necesarias.

v0_m_s = v0 * (1000 / 3600)
a_km_h = a * (3600 / 1000)

# 4) Utilizar los valores numéricos en las expresiones matemáticas de cada ecuación y obtener el valor de:

#     i. Posición final 

x = x0 + v0_m_s * t + (1/2) * a * t ** 2

#     ii. Velocidad final.

v = v0 + a_km_h * t

# 5) Reportar el resultado de la operación con el formato solicitado.

print(f"La posición final es de {x:.2f} m y la velocidad es de {v:.3f} km/h")

## ☝️ Escriba su código ENCIMA de esta línea ☝️ ## """

# Número sucesor --------------------------------------------------------------------------------------------------------------

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 3 líneas de código)

# Entrada del programa (~ 1 línea).
# Para este tipo de ejercicios no incluir ningún mensaje dentro de input, ya que cambia la respuesta que se envía y el caso no es aceptado

""" numero_n = int(input())

# Operación matemática y asignación (~ 1 línea).

numero_n_1 = numero_n + 1

# Salida del programa (~ 1 línea).

print(numero_n_1)

# Transformando cadenas de texto """

"""
Realizar un programa que reciba una cadena de texto, aplique una serie de transformaciones, siguiendo las reglas escritas a continuación; y al final imprima el resultado obtenido.


- Todos los caracteres deben de estar completamente en minúscula.
- Las vocales 'a', 'e' y 'o' deben de ser reemplazadas por el carácter 'i'.
- De igual manera, se deberán reemplazar sus versiones con acento ('Á', 'á', 'É', 'é', 'Ó' y 'ó') por el carácter 'í'.
"""

### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 11 líneas de código)

""" # Entrada del programa (~ 1 línea).
cadena = input()
cadena = cadena.lower()

# Operaciones en cadenas de texto (~ 9 líneas)
resultado = cadena.replace('a','i')
resultado = resultado.replace('e','i')
resultado = resultado.replace('o','i')
resultado = resultado.replace('á','í')
resultado = resultado.replace('é','í')
resultado = resultado.replace('ó','í')

# Salida del programa (~ 1 línea).
print(resultado) """

""" 🧩 Ejemplos

Entrada 1
Bienvenido al curso de programación con Python

Salida 1
biinvinidi il cursi di prigrimiciín cin pythin

Entrada 2
El único modo de hacer un gran trabajo es amar lo que haces

Salida 2
il únici midi di hicir un grin tribiji is imir li qui hicis

Entrada 3
Si no sueltas el pasado, ¿con qué mano agarras el futuro?

Salida 3
si ni suiltis il pisidi, ¿cin quí mini igirris il futuri? """

# ---------------------------------------------------------------------------------------------------------------------------------

""" 💡 Problema: División de las ganancias

Escriba un programa que solucione el siguiente problema algebraico.


Decide poner un puesto de venta de tamales en una feria local con 6
 de sus amigos. Preparar un tamal tiene un valor de 3$
, por lo que entre todos deciden vender los tamales a 5$
 para tener un margen de ganancias apropiado. De antemano acuerdan que las ganancias de las ventas serán divididas entre los 7
 de manera equitativa y sin partes d ecimales, y el dinero que sobre será guardado para ser usado en una celebración después del evento.


Por ejemplo, si el dinero recolectado al final del evento, descontando el dinero invertido en cocinar los tamales vendidos (es decir, la ganancia neta) es de 25$
, se podría dar 3$
 a cada uno de los amigos y quedarían 4$
 para la celebración.


¿Cuánto dinero le corresponde a cada persona y cuánto dinero queda para la reunión?

⌨️ Entrada

¿Cómo funciona la entrada en UNCode?
La entrada será provista por UNCode en la forma de casos de prueba de texto. Esta entrada deberá ser recibida en su programa con instrucciones que incluyan la función input.

El programa recibirá un único valor de entrada.


- ventas: número entero entre 0 y 300 que representa el número total de tamales vendido.


🖥️ Salida

¿Cómo funciona la salida en UNCode?
La salida será capturada por UNCode y comparada con la salida esperada de cada caso de prueba. Esta salida deberá ser generada por su programa con instrucciones que incluyan la función print.


El programa debe imprimir en la salida dos líneas.

- monto_integrante: el monto de dinero que le corresponde a cada integrante del grupo.
- monto_sobrante: el monto de dinero sobrante y depositado para la celebración después del evento. 

🧩 Ejemplos

Entrada Ejemplo 1           Salida Ejemplo 1
93                          26
                            4

Entrada Ejemplo 2           Salida Ejemplo 2
21                          6
                            0

Entrada Ejemplo 3           Salida Ejemplo 3
2                           0
                            4
"""
### ESCRIBA SU CÓDIGO A PARTIR DE AQUÍ ### (~ 6 líneas de código)

# Entrada del programa (~ 1 línea).
ventas = int(input())                       # Reemplace 'None' por el código necesario. 

if ventas in range(0,301): 

    costo = 3 * ventas
    total = 5 * ventas
    ganancias = total - costo

    # Operaciones matemáticas (~ 3 líneas).

    monto_integrante = ganancias // 7
    monto_sobrante = ganancias % 7

    # Salida del programa (~ 2 líneas).
    print(monto_integrante)          # Indique el primer resultado en esta línea.
    print(monto_sobrante)            # Indique el segundo resultado en esta línea.