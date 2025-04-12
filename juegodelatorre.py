import random

opciones = ["piedra", "papel", "tijera"]

while True:
    jugador = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    if jugador == "salir":
        break

    if jugador not in opciones:
        print("Opción no válida, intenta de nuevo.")
        continue

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Empate!")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "tijera" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")

print("Gracias por jugar.")
