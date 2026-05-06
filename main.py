from src.clases import Producto, Proveedor, Periodo
from src.modelo import resolver
from src.solucion import mostrar_solucion


# Test 1: Stock inicial 0, demanda fija, un producto, un proveedor

print("TEST 1")

productos = [Producto("P1", "Leche", 10, 0)]
proveedores = [Proveedor("S1", "Proveedor A", 0, 5, ["P1"])]
periodos = [Periodo(1, {}), Periodo(2, {}), Periodo(3, {})]

precios = {("P1", "S1"): 2.0}
costes = {("P1", "S1"): 0.5}
coste_almacen = {"P1": 0.01}  
stock_inicial = {"P1": 0}
demanda = {("P1", 1): 10, ("P1", 2): 10, ("P1", 3): 10}
capacidad_almacen = 500

problema, compras, stock, pedido = resolver(
    productos, proveedores, periodos, precios, costes,
    coste_almacen, stock_inicial, demanda, capacidad_almacen
)
mostrar_solucion(problema, compras, stock, pedido, productos, proveedores, periodos)



# Test 2: El stock inicial cubre toda la demanda

print("\nTEST 2")

productos2 = [Producto("P1", "Harina", 10, 0)]
proveedores2 = [Proveedor("S1", "Proveedor A", 0, 5, ["P1"])]
periodos2 = [Periodo(1, {}), Periodo(2, {}), Periodo(3, {})]

precios2 = {("P1", "S1"): 2.0}
costes2 = {("P1", "S1"): 0.5}
coste_almacen2 = {"P1": 5}
stock_inicial2 = {"P1": 100}  
demanda2 = {("P1", 1): 10, ("P1", 2): 10, ("P1", 3): 10}
capacidad_almacen2 = 500

problema2, compras2, stock2, pedido2 = resolver(
    productos2, proveedores2, periodos2, precios2, costes2,
    coste_almacen2, stock_inicial2, demanda2, capacidad_almacen2
)
mostrar_solucion(problema2, compras2, stock2, pedido2, productos2, proveedores2, periodos2)



# Test 3: El producto caduca en t=1, hay 3 periodos, demanda baja
print("\nTEST 3")

productos3 = [Producto("P1", "Yogur", 1, 0)]  # caduca en t=1
proveedores3 = [Proveedor("S1", "Proveedor A", 0, 5, ["P1"])]
periodos3 = [Periodo(1, {}), Periodo(2, {}), Periodo(3, {})]

precios3 = {("P1", "S1"): 1.5}
costes3 = {("P1", "S1"): 0.3}
coste_almacen3 = {"P1": 10}
stock_inicial3 = {"P1": 0}
demanda3 = {("P1", 1): 10, ("P1", 2): 10, ("P1", 3): 10}  
capacidad_almacen3 = 500

problema3, compras3, stock3, pedido3 = resolver(
    productos3, proveedores3, periodos3, precios3, costes3,
    coste_almacen3, stock_inicial3, demanda3, capacidad_almacen3
)
mostrar_solucion(problema3, compras3, stock3, pedido3, productos3, proveedores3, periodos3)

#Test 4: la demanda= 10 pero MOQ=50 

print("\n TEST 4")
productos4 = [Producto("P1", "Harina", 10, 50)]
proveedores4 = [Proveedor("S1", "Proveedor A", 0, 0, ["P1"])]
periodos4 = [Periodo(1, {})]
precios4 = {("P1", "S1"): 2.0}
costes4 = {("P1", "S1"): 0.0}
coste_almacen4 = {"P1": 100}
stock_inicial4 = {"P1": 0}
demanda4 = {("P1", 1): 10}
capacidad_almacen4 = 500
 
problema4, compras4, stock4, pedido4 = resolver(
    productos4, proveedores4, periodos4, precios4, costes4,
    coste_almacen4, stock_inicial4, demanda4, capacidad_almacen4
)
mostrar_solucion(problema4, compras4, stock4, pedido4, productos4, proveedores4, periodos4)

#Test 5: La capacidad del almacen es de 15 y la demanda es de 20 entre los 3 periodos,
#..voy a poner que el coste del almacen es de 0 porque quiero comprobar que aun asi no me compra 20 en el periodo 1. 

print("\nTest 5")
productos5 = [Producto("P1", "Arroz", 10, 0)]
proveedores5 = [Proveedor("S1", "Proveedor A", 0, 0, ["P1"])]
periodos5 = [Periodo(1, {}), Periodo(2, {}), Periodo(3, {})]
precios5 = {("P1", "S1"): 2.0}
costes5 = {("P1", "S1"): 0.0}
coste_almacen5 = {"P1": 0}
stock_inicial5 = {"P1": 0}
demanda5 = {("P1", 1): 5, ("P1", 2): 5, ("P1", 3): 10}
capacidad_almacen5 = 15
 
problema5, compras5, stock5, pedido5 = resolver(
    productos5, proveedores5, periodos5, precios5, costes5,
    coste_almacen5, stock_inicial5, demanda5, capacidad_almacen5
)
mostrar_solucion(problema5, compras5, stock5, pedido5, productos5, proveedores5, periodos5)