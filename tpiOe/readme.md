## Sistema de gestion de clients/atencion al cliente para un taller mecanico

Este proyecto se trata un sistema simple para un taller mecánico, desarrollado en Python.
Nos permite:
* Solicitar turnos
* Consultar el estado de un vehículo
* Obtener información de contacto

El sistema funciona por consola y utiliza un archivo CSV (`turnos.csv`) para recibir y guardar los datos utilizados.


(Este Proyecto esta pensado para llevarse a cabo en lenguaje javascript para una Plataforma web (integrado en la misma pagina que se encuentra el taller mecanico))


---------------------------------------------

Como funciona?

El Sistema esta compuesto por 3 funciones y un menu principal en donde...:

# 1. Solicitar turnos

Permite al usuario solicitar un turno para reparar su auto.

Lee los días y su disponibilidad desde `turnos.csv` y asigna turnos según disponibilidad estableciendo 3 estados:

  * `disponible` pasa a `ultimo_lugar`
  * `ultimo_lugar` pasa a `completo`
Si no hay disponibilidad, sugiere otros días disponibles y guarda los cambios nuevamente en el archivo CSV

---------------------------------------------

# 2. Consulta de estado

Permite al cliente consultar el estado de su vehículo ingresando la patente.

Muestra:
* Nombre del cliente
* Estado del vehículo (en_proceso o terminado)
* Arreglos realizados
* Presupuesto

---------------------------------------------

# 3. Contacto

Brinda información sobre el taller:

* Dirección y horario de atención
* Canales alternativos

---------------------------------------------

# Menu

Muestra las siguientes opciones infinitamente hasta que el usuario salga del bucle:

1. Necesito reparar mi auto
2. Consultar el estado de mi auto
3. Contacto
4. Salir

* Se utiliza el manejo de errores con `try/except`
* Los datos se estructuraron en 2 diccionarios (uno con los datos de los usuarios y el otro con el estado de los turnos)

---------------------------------------------

# Contenido

La carpeta esta compuesta por: (1 readme.md, 1 script.py, 1 archivo.csv)

en donde turnos.csv debe tener el siguiente formato:
lunes,martes,miercoles,jueves,viernes,sabado
disponible,disponible,disponible,disponible,disponible,disponible




