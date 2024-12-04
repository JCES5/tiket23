

def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

<<<<<<< HEAD
def consultarMulta(tipomulta):
    if tipomulta == 1:
        return 10/100*100
    if tipomulta == 2:
        return 15/100*100
    if tipomulta == 3:
        return 20/100*100
    if tipomulta == 4:
        return 30/100*100
    else:
        return -1
=======
def calcularSubtotal(PrecioProducto, Cantidad, PorcentajeDescuento):
    SubtotalSinDescuento = PrecioProducto * Cantidad 
    Descuento = (SubtotalSinDescuento * PorcentajeDescuento) / 100
    Subtotal1 = SubtotalSinDescuento - Descuento
    Subtotal2 = SubtotalSinDescuento - Descuento
    Subtotal3 = SubtotalSinDescuento - Descuento
    return Subtotal1, Subtotal2,Subtotal3


>>>>>>> 17dcb30933a582812f19b49e8eb0ef87818a76bd
