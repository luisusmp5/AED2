# ==================================
# SIGER
# Sistema Inteligente de Gestión de Reciclaje
# ==================================

residuos = []

# --------------------------
# Registrar residuo
# --------------------------
def registrar_residuo():

    tipo = input("Ingrese tipo de residuo: ")
    peso = float(input("Ingrese peso (kg): "))

    residuo = {
        "tipo": tipo,
        "peso": peso
    }

    residuos.append(residuo)

    print("Residuo registrado correctamente")


# --------------------------
# Mostrar residuos
# --------------------------
def mostrar_residuos():

    if (len(residuos) == 0):
        print("No existen residuos registrados")
        return

    print("\nLISTA DE RESIDUOS")

    for i in range(len(residuos)):
        print(i + 1, "-", residuos[i]["tipo"], "-", residuos[i]["peso"], "kg")


# --------------------------
# Selection Sort
# --------------------------
def ordenar_por_peso():

    n = len(residuos)

    for i in range(n):

        menor = i

        for j in range(i + 1, n):

            if (residuos[j]["peso"] < residuos[menor]["peso"]):
                menor = j

        aux = residuos[i]
        residuos[i] = residuos[menor]
        residuos[menor] = aux

    print("Residuos ordenados por peso")


# --------------------------
# Buscar residuo
# --------------------------
def buscar_residuo():

    buscar = input("Ingrese tipo a buscar: ")

    encontrado = False

    for i in range(len(residuos)):

        if (residuos[i]["tipo"].lower() == buscar.lower()):

            print("Encontrado:")
            print(residuos[i])

            encontrado = True

    if (encontrado == False):
        print("No encontrado")


# --------------------------
# Estadísticas
# --------------------------
def estadisticas():

    total = 0

    for i in range(len(residuos)):
        total = total + residuos[i]["peso"]

    print("Cantidad de residuos:", len(residuos))
    print("Peso total reciclado:", total, "kg")


# --------------------------
# Menú
# --------------------------
opcion = 0

while (opcion != 6):

    print("\n====================")
    print("      SIGER")
    print("====================")
    print("1. Registrar residuo")
    print("2. Mostrar residuos")
    print("3. Ordenar por peso")
    print("4. Buscar residuo")
    print("5. Estadísticas")
    print("6. Salir")

    opcion = int(input("Seleccione opción: "))

    if (opcion == 1):
        registrar_residuo()

    elif (opcion == 2):
        mostrar_residuos()

    elif (opcion == 3):
        ordenar_por_peso()

    elif (opcion == 4):
        buscar_residuo()

    elif (opcion == 5):
        estadisticas()

    elif (opcion == 6):
        print("Gracias por usar SIGER")

    else:
        print("Opción incorrecta")