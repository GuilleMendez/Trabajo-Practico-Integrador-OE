#bot de gestionde clientes para un taller mecanico
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
    dias_disponibles = []
    with open("turnos.csv", encoding="utf-8") as archivo:
        dias = archivo.readline().strip().split(",")
        valores = archivo.readline().strip().split(",")
        for i in range(len(dias)):
            estados[dias[i]] = valores[i]
    dia = input("Seleccione dia (lunes-martes-miercoles-jueves-viernes-sabado): ").lower()
    if dia.lower() == "lunes" or dia.lower() == "martes" or dia.lower() == "miercoles" or dia.lower() == "jueves" or dia.lower() == "viernes" or dia.lower() == "sabado":
        if dia in estados:
            if estados[dia] == "disponible":
                estados[dia] = "ultimo_lugar"
                print(f"Listo, turno registrado para el {dia}")

            elif estados[dia] == "ultimo_lugar":
                estados[dia] = "completo"
                print(f"Listo, turno registrado para el {dia}")
    
            elif estados[dia] == "completo":
                for i in estados:
                    if estados[i] == "disponible":
                        dias_disponibles.append(i)
                print(f"Lo sentimos, no tenemos turnos disponibles para esa fecha, pero si tenemos disponible el {dias_disponibles}")
        with open("turnos.csv", "w", encoding="utf-8") as archivo:
            archivo.write("lunes,martes,miercoles,jueves,viernes,sabado\n")
            archivo.write(f"{estados['lunes']},{estados['martes']},{estados['miercoles']},{estados['jueves']},{estados['viernes']},{estados['sabado']}\n")    
    else:
        print("Dia invalido, intente nuevamente")

def consultar_estado():
    opcion = input("Ingrese su patente: ")
    for i in range(len(lista_usuarios)):
        if opcion in lista_usuarios[i]['patente']:
            print(f"Datos: Nombre:{lista_usuarios[i]['nombre']} - Estado:{lista_usuarios[i]['estado']} - Arreglos hechos:{lista_usuarios[i]['arreglos_hechos']} - Presupuesto:{lista_usuarios[i]['presupuesto']}")
            return
    print("Patente invalida, intente nuevamente")

def contacto():
    try:
        opcion = int(input("Seleccione 1 para tener informacion de donde encontrarnos o presione 2 para conocer nuestros canales de comunicacion alternativos\n"))
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