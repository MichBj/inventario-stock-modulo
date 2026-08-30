import pytest
from src.inventario import Inventario

def test_cp01_registro_stock_negativo():
    inv = Inventario()
    with pytest.raises(ValueError):
        inv.registrar_producto("P101", "Martillo", -5, 10)

def test_cp02_actualizacion_stock_valida():
    inv = Inventario()
    inv.registrar_producto("P102", "Clavos", 15, 10)
    nuevo_stock = inv.actualizar_stock("P102", -8)
    assert nuevo_stock == 7

def test_cp03_verificacion_alerta_stock_bajo():
    inv = Inventario()
    inv.registrar_producto("P103", "Pintura", 5, 10)
    assert inv.verificar_alerta_stock_bajo("P103") is True

def test_cp04_integracion_salida_y_reporte_alerta():
    inv = Inventario()
    inv.registrar_producto("P104", "Tornillos", 20, 10)
    inv.actualizar_stock("P104", -15)
    reporte = inv.obtener_reporte_alertas()
    assert len(reporte) == 1
    assert reporte[0]["id"] == "P104"

def test_cp05_prevenir_stock_negativo_en_salida():
    inv = Inventario()
    inv.registrar_producto("P105", "Lija", 10, 5)
    with pytest.raises(ValueError):
        inv.actualizar_stock("P105", -25)

def test_cp06_aceptacion_flujo_reporte_completo():
    inv = Inventario()
    inv.registrar_producto("P201", "Taladro", 2, 5)
    inv.registrar_producto("P202", "Cinta", 50, 10)
    reporte = inv.obtener_reporte_alertas()
    assert len(reporte) == 1
    assert reporte[0]["nombre"] == "Taladro"