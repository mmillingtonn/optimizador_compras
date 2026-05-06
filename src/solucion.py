import pulp

def mostrar_solucion(problema, compras, stock, pedido, productos, proveedores, periodos):
    if pulp.LpStatus[problema.status] != "Optimal":
        print("No se encontró solución óptima")
        return
    
    print(f"Coste total: {pulp.value(problema.objective):.2f}€")

    print("PLAN DE COMPRAS")
    for producto in productos:
        for proveedor in proveedores:
            for periodo in periodos:
                cantidad = pulp.value(compras[producto.id, proveedor.id, periodo.t])
                if cantidad > 0:
                    print(f"Periodo {periodo.t}: comprar {cantidad} unidades de {producto.nombre} a {proveedor.nombre}")