# proyecto-integrador-1
***
Crear el archivo main del proyecto ✅  

Pedir el nombre del jugador por teclado ✅  

Imprimir un mensaje de bienvenida con el nombre ✅  

***
Parte 2:
***
Instalar la librería: https://pypi.org/project/readchar/ ✅  

Investigrar cómo leer un caracter del teclado ✅  

Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP ✅  

***
Parte 3
***

Proyecto integrador parte 3
Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:

Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, borrar la terminal y e imprimir el nuevo número hasta el número 50.

La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.

Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os

***
Parte 4
***

1. Implementar una función que reciba el mapa de un laberinto en forma de cadena, y lo convierta a matriz de caracteres.
Para generar los laberintos, usar esta página: https://www.dcode.fr/maze-generator con las configuraciones
        USE THIS CHARACTER FOR WALLS: #
        USE THIS CHARACTER FOR PATHS: .
        SINGLE CHARARACTER (MORE RECTANGULAR)
    Completar los dos caracteres de paredes faltantes al final.
    Los puntos inicial y final deben ser dados al crear el juego, usar las coordenadas (0,0) para el inicio y (end, end) para el final (Asegurarse que las coordenadas son caminos válidos)
    Recuerdo: Para separar por filas usar split("\n") y para convertir una cadena a una lista de caracteres usar list(cadena).
2. Escribir una función que limpie la pantalla y muestre la matriz (recibe el mapa en forma de matriz)
Implementar el main loop en una función (recibe el mapa en forma de matriz)
recibir: mapa List[List[str]], posicion inicial Tuple[int, int], posicion final Tuple[int, int].
definir dos variavles px y py que contienen las coordenadas del jugador, iniciar como los valores de la posición incial
procesar mientras (px, py) no coincida con la coordenada final.
asignar el caracter P en el mapa a las coordenadas (px, py) en todo momento.
leer del teclado las teclas de flechas, antes de actualizar la posición, verificar si esta posición tentativa:
No se sale del mapa
No es una pared
Si la nueva posición es válida, actualizar (px, py), poner el caracter P en esta nueva coordenada y restaurar la anterior a .
mostrar