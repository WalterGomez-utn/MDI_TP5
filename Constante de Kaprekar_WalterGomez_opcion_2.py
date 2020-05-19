# UTN - Metodologia de la investigación - Profesor Carlos Rodriguez
# desarrollo del tp5
# el ejercicio propuesto es la constante de Kaprekar
# pedimos el número de 4 digitos a ingresar
"""
el matematico Indio Dattaraya Ramchandra Kaprekar descrubrió en 1949 una curiosa característica
del número 6174. Hoy, se conoce a dicho número como constante de Kaprekar en honor a él.
el número es notable por la siguiente propiedad:
1- Elige un número de cuatro digitos que tenga, al menos dos diferentee (es válido colocar
el digito 0  al principio, por lo que el número 0009 es válido).
2-coloca sus dígitos en orden ascendente y en orden descendente para formar dos nuevos números
Puedes añadir los digitos 0 que necesites al principio
3-Restar el menor al mayor
4-vuelve al paso 2
"""
# defino las funciones para el desarrollo  del calculo de la constante de Kaprekar

def validoNro(numero):  # verifico el numero ingresado y lo casteo a str para comprarlo
    n = str(numero)
    numeroCorrecto = True
    for i in n:
        codigoASCII = ord(i)
        if codigoASCII < 48 or codigoASCII > 57:  # codigo ASCII que van desde el 0 al 9
            numeroCorrecto = False
    if numeroCorrecto:  #Si ingreso cifras menor a 4 digitos completo con ceros al inicio agregarlos
        if len(n) == 1:
            n = '000' + n  # para el caso de un digito
        else:
            if len(n) == 2:  # para el caso de dos digitos
                n = '00' + n
            else:
                if len(n) == 3:  # para el caso de tres digitos
                    n = '0' + n
        return nrosDiferentes(n)
    return False

def nrosDiferentes(numero):  # verifico que los numeros no sean todos iguales
    digito_1 = int(numero[0]) # defino a la variable con int
    cont = 0
    while cont < len(numero) - 1:  # genero el bucle que realizar la comparación con cada digito
        cont += 1
        digito_2 = int(numero[cont]) # defino una segunda variable para comprarlo con el siguiente
        if digito_1 != digito_2:
            return True
    return False

def numMay(numero):  # determino en número mayor patiendo del número ingresado
    n = str(numero)
    # Si faltan ceros al inicio agregarlos
    if len(n) == 1:  # para el caso que sea de una solo digito
        n = '000' + n
    else:
        if len(n) == 2:  # para el caso  que sea de dos digitos
            n = '00' + n
        else:
            if len(n) == 3:   # para el caso que sea de tres digitos
                n = '0' + n

    cifraMayor = ""
    cifraCompleta = False

    numAux = 0
    while cifraCompleta == False:
        mayor = int(n[0])
        cont = 0
        while cont < len(n) -1:
            cont += 1
            digito = int(str(n[cont]))
            if digito > mayor:
                mayor = digito
                numAux = cont

        cifraMayor +=str(mayor)
        n = n.replace(str(mayor), "", 1)

        if len(cifraMayor) == 4:
            cifraCompleta = True
    return int(cifraMayor)

def Kaprekar(numero):  # parte del codigo donde se calcula la constante de Kaprekar
    restaNros, nroIteraciones, nroMayor, nroMenor, numMen = (0,0,0,0,"")

    while restaNros != 6174:
        nroMayor = numMay(numero)  # determinación del número mayor
        numMayor = str(nroMayor)
        nroMenor = int(numMayor[::-1]) # determinacón del número menor
        restaNros = nroMayor - nroMenor # se realizar resta entre número mayor y menor
        nroIteraciones += 1
        numero = restaNros
        if nroIteraciones == 8:
            return 8
    return nroIteraciones

#sección del codigo donde realiza el pedido de datos y salida por consola de los resultados

cantNroCalcular = int(input("Ingresa la cantidad  de número(s) a caclcular : "))
cont = 1
while cont <= cantNroCalcular:
    numeroIng = int(input("Digite el número (no mayor de 4 digitos) :  "))
    if numeroIng == 6174:
        print("0")
    else:
        if validoNro(numeroIng):
            # posibilidad de imprimir el número ingresado  y la cantidad de iteraciones
            # print("El numero: "+ str(numeroIng) + ", Iteraciones: " + str(Kaprekar(numeroIng)))
            print(str(Kaprekar(numeroIng)))
        else:
            print('8')
    cont += 1


