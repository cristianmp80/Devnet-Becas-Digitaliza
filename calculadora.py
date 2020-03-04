#Calculadora en modo consola
#Autor: Cristian Moya Perea

import os
import math

def borrarPantalla(): 
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")


while (True):
    borrarPantalla()
    print("----------CALCULADORA-----------")
    print(" 1. Suma                        ")
    print(" 2. Resta                       ")
    print(" 3. Multiplicacion              ")
    print(" 4. Division                    ")
    print(" 5. Potencia                    ")
    print(" 6. Raiz cuadrada               ")
    print(" 7. Resto                       ")
    print(" 8. Logaritmo                   ")
    print(" 0. Salir                       ")
    print("--------------------------------")
    op = -1
    while (op<0 or op>8):
        op = int(input("\nSelecciona una operacion: "))
    if (op==0):
        print("Saliendo.")
        break

    x = float(input("\nDame el primer operando: "))
    y = float(input("Dame el segundo operando: "))

    if (op==1):
        resultado = x+y
    elif (op==2):
        resultado = x-y
    elif (op==3):
        resultado = x*y
    elif (op==4):
        resultado = x/y
    elif (op==5):
        resultado = x**y
    elif (op==6):
        resultado = math.sqrt(x)
    elif (op==7):
        resultado = x%y
    elif (op==8):
        resultado = math.log(x,y)
    else:
        input("\nOperacion incorrecta, pulse una tecla para continuar...")
        continue
    print("El resultado de la operación es:", resultado)
    input("\nPulse una tecla para continuar...")

        