# Verificar palabras ingresadas -> funcion para verificar
def verificar_palabras(secreta, ingresada):
    letras_verificadas = []
    cantidad_de_letras = 5

    palabra_ingresada_convertida = list(ingresada)
    palabra_secreta_convertida = list(secreta)

    for index in range(cantidad_de_letras):

        letra_a_verificar = palabra_ingresada_convertida[index]

        letras_son_iguales = letra_a_verificar == palabra_secreta_convertida[index]

        letra_en_palabra = letra_a_verificar in secreta

        if letras_son_iguales:
            letras_verificadas.append("[" + letra_a_verificar + "]")
        elif letra_en_palabra:
            letras_verificadas.append("(" + letra_a_verificar + ")")
        else:
            letras_verificadas.append(letra_a_verificar)
    
    return letras_verificadas


def imprimir_grilla (lista_de_listas):
    cantidad_de_listas = len(lista_de_listas)
    for i in range(cantidad_de_listas):
        print(lista_de_listas[i])


palabra_secreta = "calor"
cantidad_de_letras = 5
intentos = 6

grilla = []

# Intentos  -> Si nos quedamos sin intentos, hule

# Usar un while

print("Bienvenido a WORDLEn't")

while intentos > 0:
    print("Te quedan" + str(intentos) + "intentos.")
    palabra_ingresada = input("Ingrese una palabra: ")
    intentos = intentos - 1

    letras_de_palabra_ingresada = list(palabra_ingresada)
    letras_de_palabra_secreta = list(palabra_secreta)

    cantidad_de_letras_de_palabra_ingresada = len(palabra_ingresada)

    if(cantidad_de_letras_de_palabra_ingresada != cantidad_de_letras):
        print("La palabra ingresada no tiene la cantidad de letras correcta.")
        print("Ingresar una palabra con " + str(cantidad_de_letras) + "letras.")
    else:
        linea_verificada = verificar_palabras(palabra_secreta, palabra_ingresada)
        grilla.append(linea_verificada)

    imprimir_grilla(grilla)

    if palabra_ingresada == palabra_secreta:
        print("Felicidades, ganaste! 🎉")
        break
