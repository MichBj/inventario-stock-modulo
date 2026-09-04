class ProductoInventario:
    def __init__(self, codigo: str, nombre: str, stock: int, umbral_minimo: int):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock
        self.umbral_minimo = umbral_minimo

    def registrar_salida(self, cantidad: int):
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad


class GestionInventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto: ProductoInventario):
        self.productos[producto.codigo] = producto

    def obtener_producto(self, codigo: str):
        return self.productos.get(codigo)