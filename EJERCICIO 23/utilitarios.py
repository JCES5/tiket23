def calcularPromedio(val1,val2,val3):
    calculo=val1+val2+val3
    promedio1=calculo/3
    return promedio1

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
