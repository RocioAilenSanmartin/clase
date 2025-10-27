"""
La trifecta- Requisitos a cumplir
Al iniciar se nos debe pedir ingresar un numero entero, si este es distinto a 0 el programa inicia, de lo contrario finaliza (tambien si se ingresa otra cosa que no sea un numero entero).
Se debe poder ingresar una Palabra o Frase y contar cuantos caracteres tiene dicha palabra o frase
Con el valor obtenido en el punto anterior calcular su Factorial, una vez hecho esto , decirnos si el resultado es par o impar.
Se deben imprimir los resultados por pantalla en cada paso.
Una vez cumplido esto, deberemos volver a pedir el ingreso de un número y realizar la verificación del punto 1
"""
incorrecto= True
while incorrecto:
    numero= input("Ingrese un número entero: ")   
    if numero.isdigit():
        numero=float(numero)
        if numero!=int(numero) or int(numero)==0:
                print("El programa finalizó")
                incorrecto=False
        else:
            frase=input("Ingrese una palabra o frase: ")
            cantidad=len(frase)
            print(f"La cantidad de caracteres que posee la frase es {cantidad}")
            factorial=1
            for i in range (1,cantidad+1):
                factorial=factorial*i
            print(f"El factorial de la cantidad de caracteres es {factorial}")
            par_o_impar=factorial % 2
            if par_o_impar==0:
                print("El factorial de la cantidad de caracteres es par")
            else:
                print("El factorial de la cantidad de caracteres es impar")  
    else:
        print("El programa finalizó")
        incorrecto=False
