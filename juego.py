from asyncio import sleep
import os
import flota


def bienvenida():
    os.system('cls')
    print("¡Bienvenido al juego de Battleship!")
    print("Prepárate para una batalla naval estratégica.")
    print("Tu objetivo es hundir todos los barcos de tu oponente antes de que él hunda los tuyos.")
    print("Vas a jugar contra la computadora, así que planifica bien tus movimientos.")
    print("¡Buena suerte y que comience la batalla!")
    return None

def imprimir_tabla_vacia():
    print("  " + "   ".join([str(i+1) for i in range(10)]))  # Encabezado de columnas
    for i in range(10):
        fila = f"{i+1} " + "|".join(["   " for _ in range(10)])
        print(fila)
        if i < 9:
            print("  " + "---+"*9 + "---")
    return None

def crear_tablero():
    return [[" " for _ in range(10)] for _ in range(10)]

def imprimir_tabla(matriz):
    print("   " + "   ".join([str(i+1) for i in range(10)]))  # Encabezado de columnas
    print("-----------------------------------------")
    for i in range(10):
        print(f"{i+1} | " + " | ".join(matriz[i]) + " |")
        print("-----------------------------------------")
    return matriz

# Ejemplo de uso
bienvenida()
imprimir_tabla_vacia()

# Crear las dos matrices de 10x10
mapa1 = [[" " for _ in range(10)] for _ in range(10)]
mapa2 = [[" " for _ in range(10)] for _ in range(10)]

bienvenida()

print("\n¡Listo para jugar!")
print("¡Buena suerte y que comience la batalla!")
input("\nPresiona Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')

print("USTED SERÁ JUGADOR 1\nJUGADOR 2 ES LA COMPUTADORA")
print("Coloque sus barcos en el mapa...\n\n")
print("Coloque su Portavion en el mapa")
input("Presiona Enter para continuar...")
fila=int(input("Ingrese la fila donde desea colocar el Portavion: "))-1
columna=int(input("Ingrese la columna donde desea colocar el Portavion: "))-1
direccion=input("Ingrese la dirección del Portavion (H/V): ").upper()
flota.nave(mapa1, fila, columna, direccion, "P",4)
os.system('cls' if os.name == 'nt' else 'clear')
print("\nMapa con su Portavion colocado, esta es su distribución actual:\n")
imprimir_tabla(mapa1)
input("\nPresiona Enter para continuar...")
os.system('cls' if os.name == 'nt' else 'clear')

# Colocar 3 Acorazados o Submarinos
for _ in range(3):
    barco = input("Pulse A para colocar un Acorazado, pulse S para colocar un Submarino:\n ").upper()
    if barco == "A":
        fila=int(input("Ingrese la fila donde desea colocar el Acorazado: "))-1
        columna=int(input("Ingrese la columna donde desea colocar el Acorazado: "))-1
        direccion=input("Ingrese la dirección del Acorazado (H/V): ").upper()
        flota.nave(mapa1, fila, columna, direccion, "A",3)
    elif barco == "S":
        fila=int(input("Ingrese la fila donde desea colocar el Submarino: "))-1
        columna=int(input("Ingrese la columna donde desea colocar el Acorazado: "))-1
        direccion=input("Ingrese la dirección del Acorazado (H/V): ").upper()
        flota.nave(mapa1, fila, columna, direccion, "S",3)
        

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nMapa con su barco colocado, esta es su distribución actual:\n")
    imprimir_tabla(mapa1)
    input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
    
print("Ahora procederemos a colocar los destructores")
input("Presiona Enter para continuar...")
os.system('cls')

for _ in range(3):
    fila=int(input("Ingrese la fila donde desea colocar el Destructor: "))-1
    columna=int(input("Ingrese la columna donde desea colocar el Destructor: "))-1
    direccion=input("Ingrese la dirección del Destructor (H/V): ").upper()
    flota.nave(mapa1, fila, columna, direccion, "D",2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nMapa con su Destructor colocado, esta es su distribución actual:\n")
    imprimir_tabla(mapa1)
    input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')


print("Por ultimo,vamos a colocar las fragatas! \n\n")
input("Presiona Enter para continuar...")
os.system('cls')

for _ in range(2):
    fila=int(input("Ingrese la fila donde desea colocar la Fragata: "))-1
    columna=int(input("Ingrese la columna donde desea colocar la Fragata: "))-1
    direccion=input("Ingrese la dirección de la Fragata (H/V): ").upper()
    flota.nave(mapa1, fila, columna, direccion, "F",1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nMapa con su Fragata colocada, esta es su distribución actual:\n")
    imprimir_tabla(mapa1)
    input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

print("¡Listo para jugar!\n\n")
print("Ahora haremos lo mismo con la computadora pero de forma aleatoria!")
print("Preparando en 3\n")
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("Preparando en 2\n")
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("Preparando en 1\n")
sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')
print("Colocando barcos de la computadora...\n\n")
input("Presiona Enter para continuar...")
print("La computadora ha colocado sus barcos, ahora es tu turno de jugar!")
input("\nPresiona Enter para continuar...")
os.system('cls')
flota.generate_enemy(mapa2)
os.system('cls')

print("¡Listo para jugar!")
print("¡Buena suerte y que comience la batalla!")
input("\nPresiona Enter para continuar...")
print("ESTE ES TU MAPA:\n\n\n")
imprimir_tabla(mapa1)
print("*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*")
vertical = int(input("Ingrese la fila donde desea disparar: "))-1
horizontal = int(input("Ingrese la columna donde desea disparar: "))-1
flota.turno(mapa2,horizontal,vertical)
flota.turno_enemy(mapa1)
os.system('cls')









