class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historiar = []

    def responder(self, mensaje):
        self.historiar.append(mensaje)

        if "hola" in mensaje.casefold() or "buenas" in mensaje.casefold():
            respuesta = f"Hola, bienvenido/a a {self.nombre_negocio}."
        else:
            respuesta = "No entiendo tu mensaje."

        self.historiar.append(respuesta)
        return respuesta
