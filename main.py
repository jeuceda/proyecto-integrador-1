import readchar

nombre_jugador = input('Ingresa el nombre del Jugador: ')

print('Bienvenido al juego, {}!'.format(nombre_jugador))

#Parte 2:

while True:
    keypress = readchar.readkey()
    if keypress == readchar.key.UP:
        break
    print(keypress)

# Parte 3:

def limpiar_terminal():
  import os
  import subprocess
  if os.name == 'nt':
    subprocess.call('cls')
  else:
    subprocess.call('clear')

def imprimir_numero(numero):
  print(numero)

numero = 0

while numero <= 50:
  limpiar_terminal()
  imprimir_numero(numero)
  numero += 1
  entrada = input("Pulse n para continuar: ")
  if entrada == "n":
    continue
  else:
    break
