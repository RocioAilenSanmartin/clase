#Adivina el número
"""
Se busca crear un juego para adivinar un numero generado de manera random, para ello deberemos 
implementar Variables, Bucles, Condicionales, Operadores Logicos, Operadores Aritmeticos,
Asignación de valores, Input, Print
Requisitos a cumplir:
El juego termina cuando el Jugador acierta el numero o hace 5 intentos.
Cuando se pide ingresar el número se le debe indicar al jugador el rango máximo y mínimo.
Si el jugador falla, se debe indicar si el número es mayor o menor.
Al perder se le enviara un mensaje indicandole que ha perdido y cual era el número.
"""
import random
numero_secreto= random.randint(0,50)
print("A continuación, usted intentará adivinar un número secreto")
contador=0
print(numero_secreto)
while True:
    if contador < 5:
        numero_ingresado=input("Ingrese un número entero entre 0 y 50: ")
        if numero_ingresado.isdigit():
            numero_ingresado= int(numero_ingresado)
            if 0<=numero_ingresado<=50 and not numero_ingresado == numero_secreto :
                if numero_ingresado < numero_secreto :
                    print("Debe ingresar un número más grande")
                else:
                    print("Debe ingresar un número más chico")
                contador=contador+1
            elif numero_ingresado<0 or numero_ingresado>50:
                print("Solo puede ingresar números entre 0 y 50")
            else:
                print(f"End Game: Usted adivinó que el número es {numero_secreto}")
                break 
        else:
                print("Solo puede ingresar números")     
    else : 
        print(f"End game: Usted no adivinó el número. La respuesta correcta era {numero_secreto}")
        break
    


#Adivina el número
"""
Se busca crear un juego para adivinar un numero generado de manera random, para ello deberemos 
implementar Variables, Bucles, Condicionales, Operadores Logicos, Operadores Aritmeticos,
Asignación de valores, Input, Print
Requisitos a cumplir:
El juego termina cuando el Jugador acierta el numero o hace 5 intentos.
Cuando se pide ingresar el número se le debe indicar al jugador el rango máximo y mínimo.
Si el jugador falla, se debe indicar si el número es mayor o menor.
Al perder se le enviara un mensaje indicandole que ha perdido y cual era el número.
"""
import random
numero_secreto= random.randint(0,50)
print("A continuación, usted intentará adivinar un número secreto")
contador=0
print(numero_secreto)
while True:
    if contador < 5:
        numero_ingresado=input("Ingrese un número entero entre 0 y 50: ")
        if numero_ingresado.isdigit():
            numero_ingresado= int(numero_ingresado)
            if 0<=numero_ingresado<=50 and not numero_ingresado == numero_secreto :
                if numero_ingresado < numero_secreto :
                    print("Debe ingresar un número más grande")
                else:
                    print("Debe ingresar un número más chico")
                contador=contador+1
            elif numero_ingresado<0 or numero_ingresado>50:
                print("Solo puede ingresar números entre 0 y 50")
            else:
                print(f"End Game: Usted adivinó que el número es {numero_secreto}")
                break 
        else:
                print("Solo puede ingresar números")     
    else : 
        print(f"End game: Usted no adivinó el número. La respuesta correcta era {numero_secreto}")
        break
    

