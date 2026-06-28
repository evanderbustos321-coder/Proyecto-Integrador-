# Proyecto Integrador
# Juego: Piedra, Papel o Tijera

import random

# Variables globales
victorias = 0
derrotas = 0
empates = 0


# Función para mostrar el menú
def mostrar_menu():
    print("\n====== MENÚ ======")
    print("1. Jugar")
    print("2. Ver marcador")
    print("3. Salir")


# Función para obtener la elección del jugador
def elegir_jugada():
    while True:
        print("\nElige una opción:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijera")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            return "Piedra"
        elif opcion == "2":
            return "Papel"
        elif opcion == "3":
            return "Tijera"
        else:
            print("Opción inválida. Intente nuevamente.")


# Función para la elección de la computadora
def jugada_computadora():
    opciones = ["Piedra", "Papel", "Tijera"]
    return random.choice(opciones)


# Función para comparar las jugadas
def determinar_ganador(jugador, computadora):
    global victorias, derrotas, empates

    print("\nTú elegiste:", jugador)
    print("La computadora eligió:", computadora)

    if jugador == computadora:
        print("Empate.")
        empates += 1

    elif (
        (jugador == "Piedra" and computadora == "Tijera") or
        (jugador == "Papel" and computadora == "Piedra") or
        (jugador == "Tijera" and computadora == "Papel")
    ):
        print("¡Ganaste!")
        victorias += 1

    else:
        print("Perdiste.")
        derrotas += 1


# Función para mostrar el marcador
def mostrar_marcador():
    print("\n====== MARCADOR ======")
    print("Victorias:", victorias)
    print("Derrotas:", derrotas)
    print("Empates:", empates)


# Función principal
def main():

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            jugador = elegir_jugada()
            computadora = jugada_computadora()
            determinar_ganador(jugador, computadora)

        elif opcion == "2":
            mostrar_marcador()

        elif opcion == "3":
            print("\nGracias por jugar.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Inicio del programa
main()