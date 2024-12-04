

def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

def calcularSubtotal(PrecioProducto, Cantidad, PorcentajeDescuento):
    SubtotalSinDescuento = PrecioProducto * Cantidad 
    Descuento = (SubtotalSinDescuento * PorcentajeDescuento) / 100
    Subtotal1 = SubtotalSinDescuento - Descuento
    Subtotal2 = SubtotalSinDescuento - Descuento
    Subtotal3 = SubtotalSinDescuento - Descuento
    return Subtotal1, Subtotal2,Subtotal3


