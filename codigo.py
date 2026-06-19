#bot de gestion de clientes para un taller mecanico
#lenguaje: js, plataforma:web (instegrado en la misma pagina donde vendemos nuestros productos)
#interaccion con base de datos
#diccionario de datos-base de datos-estados
#repositorio en github con readme(manual de usuario)
#manejo de errores

#variables
estados = {}
lista_usuarios = [
    {"nombre":"miranda", "patente":"14n1yu52", "estado":"en_proceso", "arreglos_hechos":"Suspensión deportiva", "presupuesto":"159800"},
    {"nombre":"micaela", "patente":"u3252a52", "estado":"terminado", "arreglos_hechos":"Llantas nuevas", "presupuesto":"670000"},
    {"nombre":"lucas", "patente":"7133uhg4", "estado":"terminado", "arreglos_hechos":"Revisión de frenos", "presupuesto":"123400"},
    {"nombre":"jorge", "patente":"6t43z714", "estado":"terminado", "arreglos_hechos":"Control de batería", "presupuesto":"63400"},
    {"nombre":"diana", "patente":"71x4s357", "estado":"en_proceso", "arreglos_hechos":"", "presupuesto":"95000"}
]

#funciones
def reparacion():
    estados = {}

    # Leer archivo
    with open("turnos.csv", encoding="utf-8") as archivo:
        dias = archivo.readline().strip().split(",")
        valores = archivo.readline().strip().split(",")
        for i in range(len(dias)):
            estados[dias[i]] = valores[i]

    dia = input("Seleccione día (lunes-martes-miercoles-jueves-viernes-sabado): ").lower()

    if dia not in estados:
        print("Día inválido, intente nuevamente")
        return

    # Lógica de reserva SOLO para el día elegido
    if estados[dia] == "disponible":
        estados[dia] = "ultimo_lugar"
        print(f"Listo, turno registrado para el {dia}")

    elif estados[dia] == "ultimo_lugar":
        estados[dia] = "completo"
        print(f"Listo, turno registrado para el {dia}")

    elif estados[dia] == "completo":
        # Buscar otros días disponibles
        dias_disponibles = [d for d in estados if estados[d] == "disponible"]
        if dias_disponibles:
            print(f"No hay turnos para ese día, pero sí para: {dias_disponibles}")
        else:
            print("No quedan turnos disponibles en toda la semana")

    # Guardar cambios
    with open("turnos.csv", "w", encoding="utf-8") as archivo:
        archivo.write(",".join(estados.keys()) + "\n")
        archivo.write(",".join(estados[d] for d in estados) + "\n")


def consultar_estado():
    opcion = input("Ingrese su patente: ")
    for i in range(len(lista_usuarios)):
        if opcion in lista_usuarios[i]['patente']:
            print(f"Datos: Nombre:{lista_usuarios[i]['nombre']} - Estado:{lista_usuarios[i]['estado']} - Arreglos hechos:{lista_usuarios[i]['arreglos_hechos']} - Presupuesto:{lista_usuarios[i]['presupuesto']}")
            return
    print("Patente invalida, intente nuevamente")

def contacto():
    try:
        opcion = int(input("Seleccione 1 para tener informacion de donde encontrarnos o, presione 2 para conocer nuestros canales de comunicacion alternativos o presione 3 para volver al menú\n"))
        if opcion == 1:
            print("Nos encontramos en Pinamar - Buenos Aires, calle Dominguez 8272 de 8:00hs a 23:00hs\n")
        elif opcion == 2:
            print("Whatsapp 1149387464 - Instagram mecanilandia.ok - Gmail mecanilandia@gmail.com\n")
        elif opcion == 3:
            print("Volviendo al menu...")
            return
    except ValueError as error:
        print(f"Error: {error} Debe ingresar un numero entre 1 y 3")

while True:
    try:
        opcion = int(input("Bienvenido al sistema de atencion al cliente...\nSeleccione una de las siguientes opciones:(1, 2, 3 o 4)\n1. Necesito reparar mi auto \n2. Consultar el estado de mi auto \n3. Contacto\n4. Salir\n"))
        if opcion == 1:
            reparacion()
        elif opcion == 2:
            consultar_estado()
        elif opcion == 3:
            contacto()
        elif opcion == 4:
            print("saliendo...")
            break

    except ValueError as error:
        print(f"Error: {error} Debe ingresar un numero entre 1 y 4")