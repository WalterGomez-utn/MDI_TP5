# UTN - Metodologia de la investigación - Profesor Carlos Rodriguez
# desarrollo del tp5
# el ejercicio propuesto es la constante de Kaprekar
# pedimos el número de 4 digitos a ingresar

def inicio():
    # ----------------------------------------------------
    # se genera le pedido del dato para realizar el calculo
    print("-----------------------------------------------------------------------------")
    print("recuerde que no debe ingresar 4 dígitos iguales, (ej.: 1111),")
    print("para ese caso el cáculo de Constante de Kaprekar no se puede realizar")
    print("-----------------------------------------------------------------------------")
    sNro = input("\nPor favor, ingrese un número de 4 digitos, y al menos 2 de ellos diferentes : ")
    print(("El dato ingresado es :"), sNro)

    # -----------------------------------------------------
    # sección del codigo donde se genera la validación
    # para que el dato ingresado no sea todos iguales
    # genero una serie de condicionales para comparar caracter por caracter
    # y luego si se determina que todos los caracteres son iguales imprima un mensaje de error

    for i, caracter in enumerate(sNro):  # bucle para comprar si cada digito es igual al anterior
        if i == 0:
            pass
        else:
            if len(sNro) == 4:
                if (sNro[i-1] == sNro[i] and sNro[i-2] == sNro[i] and sNro[i-3] == sNro[i]):  # comparo cada caracter con los anteriores
                    print("ERROR, el dato ingresado es 4 digitos/letras iguales (imposible calcular la Constante de Kaprekar) ...")
                    restart = input("\nDesea digitar un número (de 4 dígitos ) nuevamente (s/n): ").lower()
                    # condicional que habilita salir o continuar en el programa
                    if restart == "s":
                        inicio()  # acción que hace que se vuelva al inicio del programa
                    else:
                        exit()  # genera la salida del programa

    # -----------------------------------------------------
    # sección del codigo donde se genera la validación
    # para que el dato ingresado no sea superior a 4 digitos
    if len(sNro) > 4:
        print("ERROR, el dato ingresado supera los 4 digitos ...")
        restart = input("\nDesea digitar un número (de 4 dígitos) nuevamente (s/n): ").lower()
        # condicional que habilita salir o continuar en el programa
        if restart == "s":
            inicio()  # acción que hace que se vuelva al inicio del programa
        else:
            exit()  # genera la salida del programa

    # ----------------------------------------------------------
    # sección del código donde se desarrolla la excepción para validar el número ingresado
    # desplegando la posibilidad de salir del programa
    try:
        nro=int(sNro)
    except:
        # despliego el mensaje de error del dato mal ingresado
        print("\n - ERROR -El dato ingresado (letra(s) o palabra(s) o simbolos ) es invalido, por favor verificar ...")
        # genero la alternativa de volver a inicio de programa
        restart = input("\nDesea digitar un número (de 4 dígitos) nuevamente (s/n): ").lower()
        # condicional que habilita salir o continuar en el programa
        if restart == "s":
            inicio()  # acción que hace que se vuelva al inicio del programa
        else:
            exit()   # genera la salida del programa

      # ------------------------------------------------------------------
      # sección del código donde se desarrolla el bucle para el calculo
      # de la constante de Kaprekar

    for k in range(99):  # maximo 99 iteraciones
        sNro = "{:04d}".format(nro)                    # si ingreso menos de 4 digitos los completo con ceros
        sNroG = "".join(sorted(sNro, reverse=True))    # ordeno el número de mayor a menor
        sNroP = "".join(sorted(sNro))                  # ordeno el número de menor a mayor
        nro= int(sNroG) - int(sNroP)                   # realizo la resta entre los números

        # imprimo o muestro por consola la secuencia de números y los resultados
        print(sNroG, (" - "), sNroP, (" = "), nro, ("iteración N° : "), "({:02d})".format(k + 1))
        if nro == 6174:  # cuando la variable nro alcanza el valor 6174 se detiene el bucle
            break

    print("-----------------------------------------------")
    print("Constante de Kaprekar ", nro, " - N° total de iteraciones :", k + 1)

       # ---------------------------------------------------------------
       # sección de código que es una variante del programa donde
       # calcula una vez alcanzado la constante de Kapreka
       # sobre ese mismo valor realiza al resta para
       # para nuevamente  obtener  la constante de Kaprekar

    # numR = 0  # declaro una variable para realizar la comparación luego
    # for k in range(99):  # maximo 99 iteraciones
    #     sNro = "{:04d}".format(nro)
    #     sNroG = "".join(sorted(sNro, reverse=True))  # ordeno el número de mayor a menor
    #     sNroP = "".join(sorted(sNro))  # ordeno el número de menor a mayor
    #     nro = int(sNroG) - int(sNroP)  # realizo la resta entre los números
    #     imprimo o muestro por consola la secuencia de números y los resultados
    #     print(sNroG, (" - "), sNroP, (" = "), nro, ("paso"), "({:02d})".format(k + 1))
    #     if nro == numR:
    #         break
    #     numR = nro
    # print("-----------------------------------------------")
    # print("Constante de Kaprekar ", nro, " - ", numR, " - N° total de iteraciones :", k + 1)

     # -------------------------------------------------------------------------------------------
    # sección del código donde donde se despliega la posibilidad de volver a realizar
    # el cálculo de la constante de Kaprekar o salir del programa

    restart = input("Desea ingresar  un número (de 4 digitos) nuevamente (s/n) : ").lower()
    # genero el condicional para optar para reinciar el programa o salir
    if restart == "s":
        inicio()
    else:
        exit()
inicio()
