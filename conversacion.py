def iniciar_conversacion(asistente):
    print(f"Bienvenido/a a {asistente.nombre_negocio}.")

    despedidas = ("adios", "bye", "chao", "hasta luego", "buenas noches", "salir")

    while True:
        mensaje = input("Tú: ")
        respuesta = asistente.responder(mensaje)
        print(respuesta)

        if any(despedida in mensaje.casefold() for despedida in despedidas):
            break

    asistente.mostrar_historiar()
