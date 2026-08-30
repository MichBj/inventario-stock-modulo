class Inventario:
    def __init__(self):
        # Almacenamiento en memoria para productos
        self.productos = {}

    def registrar_producto(self, id_prod, nombre, stock, umbral_minimo):
        if stock < 0:
            raise ValueError("El stock inicial no puede ser negativo.")
        if umbral_minimo < 0:
            raise ValueError("El umbral mínimo no puede ser negativo.")
        
        self.productos[id_prod] = {
            "id": id_prod,
            "nombre": nombre,
            "stock": stock,
            "umbral_minimo": umbral_minimo
        }
        return True

    def actualizar_stock(self, id_prod, cantidad_cambio):
        if id_prod not in self.productos:
            raise KeyError("Producto no encontrado.")
        
        nuevo_stock = self.productos[id_prod]["stock"] + cantidad_cambio
        if nuevo_stock < 0:
            raise ValueError("El stock resultante no puede ser negativo.")
            
        self.productos[id_prod]["stock"] = nuevo_stock
        return self.productos[id_prod]["stock"]

    def verificar_alerta_stock_bajo(self, id_prod):
        if id_prod not in self.productos:
            raise KeyError("Producto no encontrado.")
        
        p = self.productos[id_prod]
        return p["stock"] <= p["umbral_minimo"]

    def obtener_reporte_alertas(self):
        return [p for p in self.productos.values() if p["stock"] <= p["umbral_minimo"]]
    #prueba