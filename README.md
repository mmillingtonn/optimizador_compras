Función objetivo (C): Minimizar el coste de adquisición y distribución, dado por:
C = coste de compra + coste logístico
Objetivo: Determinar el conjunto óptimo de compras P = {pᵢ,ⱼ,ₜ}, donde cada elemento representa la cantidad comprada del producto i al proveedor j en el período t, de forma que se satisfaga la demanda proyectada, se respeten todas las restricciones y se minimice el coste total.

Para el coste logístico he tenido en cuenta tres cosas: coste de transporte por producto y proveedor, coste de almacenamiento por unidad en stock, y coste fijo por pedido.
Las restricciones implementadas son: balance de stock entre períodos, caducidad de productos, MOQ, pedido mínimo por proveedor, capacidad del almacén y productos disponibles por proveedor.

He hecho algunos tests en main comprobando las diferentes restricciones del modelo. 


