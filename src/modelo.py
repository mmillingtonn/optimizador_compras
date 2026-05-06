import pulp

def resolver(productos, proveedores, periodos, precios, costes, coste_almacen, stock_inicial, demanda, capacidad_almacen):
    problema = pulp.LpProblem("optimizador_compras", pulp.LpMinimize)

    # cuanto compro de producto i al proveedor j en periodo t
    compras = {}
    for producto in productos:
        for proveedor in proveedores:
            for periodo in periodos:
                compras[producto.id, proveedor.id, periodo.t] = pulp.LpVariable(
                    f"compra_{producto.id}_{proveedor.id}_{periodo.t}",
                    lowBound=0
                )

    # cuanto stock tengo de producto i en periodo t
    stock = {}
    for producto in productos:
        for periodo in periodos:
            stock[producto.id, periodo.t] = pulp.LpVariable(
                f"stock_{producto.id}_{periodo.t}",
                lowBound=0
            )

    # variable binaria por producto, proveedor y periodo para ver si se hace pedido de este producto a este proveedor en un periodo dado
    pedido = {}
    for producto in productos:
        for proveedor in proveedores:
            for periodo in periodos:
                pedido[producto.id, proveedor.id, periodo.t] = pulp.LpVariable(
                    f"pedido_{producto.id}_{proveedor.id}_{periodo.t}",
                    cat="Binary"
                )

    # variable binaria por proveedor y periodo para ver si se hace pedido en un periodo dado
    # es para cobrar el coste fijo una sola vez por proveedor y periodo y no por producto 
    pedido_proveedor = {}
    for proveedor in proveedores:
        for periodo in periodos:
            pedido_proveedor[proveedor.id, periodo.t] = pulp.LpVariable(
                f"pedido_proveedor_{proveedor.id}_{periodo.t}",
                cat="Binary"
            )

    # Funcion objetivo = coste_compra + coste_logistico
    coste_compra = pulp.lpSum(
        precios[producto.id, proveedor.id] * compras[producto.id, proveedor.id, periodo.t]
        for producto in productos
        for proveedor in proveedores
        for periodo in periodos
        if producto.id in proveedor.productos_disponibles
    )

    coste_transporte = pulp.lpSum(
        costes[producto.id, proveedor.id] * compras[producto.id, proveedor.id, periodo.t]
        for producto in productos
        for proveedor in proveedores
        for periodo in periodos
        if producto.id in proveedor.productos_disponibles
    )

    coste_almacenamiento = pulp.lpSum(
        coste_almacen[producto.id] * stock[producto.id, periodo.t]
        for producto in productos
        for periodo in periodos
    )

    # coste fijo se cobra una vez por proveedor y periodo
    coste_fijo = pulp.lpSum(
        proveedor.coste_fijo * pedido_proveedor[proveedor.id, periodo.t]
        for proveedor in proveedores
        for periodo in periodos
    )

    coste_logistico = coste_transporte + coste_almacenamiento + coste_fijo
    problema += coste_compra + coste_logistico

    # Restricciones

    # Balance de stock
    for producto in productos:
        for periodo in periodos:
            compras_periodo = pulp.lpSum(
                compras[producto.id, proveedor.id, periodo.t]
                for proveedor in proveedores
            )
            if periodo.t == 1:
                problema += stock[producto.id, periodo.t] == stock_inicial[producto.id] + compras_periodo - demanda[producto.id, periodo.t]
            else:
                problema += stock[producto.id, periodo.t] == stock[producto.id, periodo.t - 1] + compras_periodo - demanda[producto.id, periodo.t]

    # Caducidad
    for producto in productos:
        for periodo in periodos:
            if periodo.t > producto.caducidad:
                for proveedor in proveedores:
                    problema += compras[producto.id, proveedor.id, periodo.t] == 0
                problema += stock[producto.id, periodo.t] == 0

    #  MOQ
    M = 100000 
    for producto in productos:
        for proveedor in proveedores:
            for periodo in periodos:
                problema += compras[producto.id, proveedor.id, periodo.t] >= producto.moq * pedido[producto.id, proveedor.id, periodo.t] #si no hay pedido compras tiene que ser 0
                problema += compras[producto.id, proveedor.id, periodo.t] <= M * pedido[producto.id, proveedor.id, periodo.t]

    # Pedido minimo por proveedor
    for proveedor in proveedores:
        for periodo in periodos:
            problema += pulp.lpSum(
                compras[producto.id, proveedor.id, periodo.t]
                for producto in productos
            ) >= proveedor.pedido_minimo * pedido_proveedor[proveedor.id, periodo.t]

    # Capacidad del almacen
    for periodo in periodos:
        problema += pulp.lpSum(
            stock[producto.id, periodo.t]
            for producto in productos
        ) <= capacidad_almacen

    # Solo comprar productos que el proveedor suministra
    for producto in productos:
        for proveedor in proveedores:
            if producto.id not in proveedor.productos_disponibles:
                for periodo in periodos:
                    problema += compras[producto.id, proveedor.id, periodo.t] == 0

    #si se hace pedido de cualquier producto al proveedor, pedido_proveedor = 1
    for proveedor in proveedores:
        for periodo in periodos:
            for producto in productos:
                problema += pedido_proveedor[proveedor.id, periodo.t] >= pedido[producto.id, proveedor.id, periodo.t]

    problema.solve(pulp.PULP_CBC_CMD(msg=0))

    return problema, compras, stock, pedido
