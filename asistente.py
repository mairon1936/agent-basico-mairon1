class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historiar = []
        self.preguntas_frecuentes = {
            "horario": "Nuestro horario de atención es de lunes a viernes de 9:00 a 18:00.",
            "ubicacion": "Nos encontramos en la avenida principal, número 123.",
            "precios": "Puedes consultar nuestros precios en el mostrador o en nuestra página web.",
        }

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta

        return "No entendí tu mensaje."

    def responder(self, mensaje):
        self.historiar.append(mensaje)
        mensaje_normalizado = mensaje.casefold()

        if "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            respuesta = f"Hola, bienvenido/a a {self.nombre_negocio}."
        else:
            respuesta = self.buscar_faq(mensaje_normalizado)

        self.historiar.append(respuesta)
        return respuesta
