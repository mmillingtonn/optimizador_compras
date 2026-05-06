class Producto:
    def __init__(self, id, nombre, caducidad, moq):
        self.id = id
        self.nombre = nombre
        self.caducidad = caducidad
        self.moq = moq

class Proveedor: 
    def __init__(self, id, nombre, pedido_minimo, coste_fijo, productos_disponibles): 
        self.id = id
        self.nombre = nombre
        self.pedido_minimo = pedido_minimo
        self.coste_fijo = coste_fijo
        self.productos_disponibles = productos_disponibles

class Periodo:
    def __init__(self, t, demanda):
        self.t = t
        self.demanda = demanda 