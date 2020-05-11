#Calculadora en modo consola
#Autor: Cristian Moya Perea

import os
import math

def borrarPantalla(): 
    if os.name == "posix":
       os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
       os.system ("cls")


def op_binaria():
    try:
        x = float(input("\nPrimer operando: "))
        y = float(input("Segundo operando: "))
        return x,y
    except:
        print("\nOperandos incorrectos...")
        return None

def suma():
    try:
        print("Introduzca los operandos.")
        x,y = op_binaria()
        print("\nLa suma es: ", x+y)
    except:
        print("No se pudo realizar la operación.")

def resta():
    try:
        print("Introduzca el minuendo y el sustraendo.")
        x,y = op_binaria()
        print("\nLa resta es: ", x-y)
    except:
        print("No se pudo realizar la operación.")

def multiplicacion():
    try:
        print("Introduzca los operandos.")
        x,y = op_binaria()
        print("\nEl producto es: ", x*y)
    except:
        print("No se pudo realizar la operación.")

def division():
    try:
        print("Introduce el dividendo y el divisor.")
        x,y = op_binaria()
        print("\nEl cociente es: ", x/y)
    except:
        print("No se pudo realizar la operación.")

def potencia():
    try:
        print("Introduce la base y el exponente.")
        x,y = op_binaria()
        print("\nLa potencia es: ", x**y)
    except:
        print("No se pudo realizar la operación.")

def raiz():
    try:
        r = float(input("Introduce el radicando: "))
        print("\nLa raiz cuadrada es: ", math.sqrt(r))
    except:
        print("\nOperación no permitida.")
    

def resto():
    try:
        print("Introduce el dividendo y el divisor.")
        x,y = op_binaria()
        print("\nEl resto de la división entera es: ", x%y)
    except:
        input("No se pudo realizar la operación. Pulsa INTRO para continuar...")




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
    print(" 0. Salir                       ")
    print("--------------------------------")
    opciones = {"1":suma, "2":resta, "3":multiplicacion, "4":division, "5":potencia, "6":raiz, "7":resto}
    op = input("Elija una opción: ")
    if op == "0":
        break
    
    try:
        opciones[op]()
        input("\n\nPulse INTRO para continuar...")
    except:
        input("\n\nOpcion inválida, pulse INTRO para continuar...")





 

        