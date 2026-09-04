import pytest
from src.inventario import ProductoInventario, GestionInventario

# Prueba 1: Registro/Agregado de producto exitoso
def test_registrar_producto_exitoso():
    gestion = GestionInventario()
    producto = ProductoInventario(codigo="FERR-002", nombre="Taladro 1/2", stock=5, umbral_minimo=2)
    gestion.agregar_producto(producto)
    assert gestion.obtener_producto("FERR-002").nombre == "Taladro 1/2"

# Prueba 2: Caso Crítico CP05 (Prevención de Stock Negativo)
def test_cp05_prevencion_stock_negativo_salida_excesiva():
    producto = ProductoInventario(codigo="FERR-001", nombre="Martillo 16oz", stock=10, umbral_minimo=5)
    with pytest.raises(ValueError, match="Stock insuficiente"):
        producto.registrar_salida(15)
    assert producto.stock == 10