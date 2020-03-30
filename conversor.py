# BIBLIOTECA 

# ESSA FUNÇÃO CONVERTE PÉS EM METROS
def pe2metro (numero):
    res = numero * 0.3048
    return print("{} Pés em Metros: {:.2f} m".format(numero,res))
    
# ESSA FUNÇÃO CONVERTE POLEGADAS EM CENTÍMETROS
def pol2cent (numero):
    res = numero * 2.54
    return print("{} Polegadas em Centímetros: {:.2f} cm".format(numero,res))

# ESSA FUNÇÃO CONVERTE JARDAS EM METROS
def jarda2metro (numero):
    res = numero / 1.094
    return print("{} Jardas em Metros: {:.2f} m".format(numero,res))

# ESSA FUNÇÃO CONVERTE MILHAS EM QUILÔMETROS
def milhas2km (numero):
    res = numero * 1.609
    return print("{} Milhas em Quilômetros: {:.2f} Km".format(numero,res))