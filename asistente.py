class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.nombre_usuario = ""
        self.historiar = []
        self.precios_servicios = {
            "corte": 15.0,
            "manicura": 20.0,
            "pedicura": 25.0,
        }
        self.preguntas_frecuentes = {
            "horario": "Nuestro horario de atención es de lunes a viernes de 9:00 a 18:00.",
            "ubicacion": "Nos encontramos en la avenida principal, número 123.",
            "precios": "Puedes consultar nuestros precios en el mostrador o en nuestra página web.",
        }

    def calcular_presupuesto(self):
        servicio = input("¿Qué servicio te interesa? ").strip().casefold()
        if servicio not in self.precios_servicios:
            return f"El servicio '{servicio}' no existe."

        try:
            cantidad = int(input("¿Cuántas veces quieres agendarlo? "))
        except ValueError:
            return "Por favor, introduce un número válido."

        costo_total = self.precios_servicios[servicio] * cantidad
        return f"El costo total es de ${costo_total:.2f}."

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta

        return "No entendí tu mensaje."

    def responder(self, mensaje):
        self.historiar.append(mensaje)
        mensaje_normalizado = mensaje.strip().casefold()

        if mensaje_normalizado.startswith("me llamo"):
            nombre = mensaje[ mensaje.casefold().find("me llamo") + len("me llamo"):].strip()
            if nombre:
                self.nombre_usuario = nombre.capitalize()
                respuesta = f"Hola, {self.nombre_usuario}, bienvenido/a a {self.nombre_negocio}."
            else:
                respuesta = self.buscar_faq(mensaje_normalizado)
        elif any(palabra in mensaje_normalizado for palabra in ("calcular", "presupuesto", "costo")):
            respuesta = self.calcular_presupuesto()
        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            if self.nombre_usuario:
                respuesta = f"Hola, {self.nombre_usuario}, bienvenido/a a {self.nombre_negocio}."
            else:
                respuesta = f"Hola, bienvenido/a a {self.nombre_negocio}."
        else:
            respuesta = self.buscar_faq(mensaje_normalizado)

        self.historiar.append(respuesta)
        return respuesta
