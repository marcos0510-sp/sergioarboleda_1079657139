# Tablas de Multiplicar con For Anidados

# Opción 1: Tablas del 1 al 10
print("TABLAS DE MULTIPLICAR (1 al 10)")
print("=" * 40)

for tabla in range(1, 11):
    print(f"\nTabla del {tabla}:")
    for numero in range(1, 11):
        resultado = tabla * numero
        print(f"{tabla} × {numero} = {resultado}")

# Opción 2: Mostrar todas las tablas en formato de matriz
print("\n" + "=" * 40)
print("TABLAS DE MULTIPLICAR EN MATRIZ")
print("=" * 40 + "\n")

# Encabezado
print("   ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print()

# Filas
for fila in range(1, 11):
    print(f"{fila:2} |", end="")
    for columna in range(1, 11):
        print(f"{fila * columna:4}", end="")
    print()

for i in range(1, 11):
    print( "tabla del " + str(i))
    for j in range(1, 11):
        print(str(i) + " x " + str(j) + " = " + str(i * j))