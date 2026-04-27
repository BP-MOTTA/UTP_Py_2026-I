def aleatorio(n=20):
    #docstring
    """Genera una lista de n valores aleatorios desde 0 a 5
    Args:
        n (Int): el numero de valores aleatorias que se desea generar
    Returns:
        list:
    """
    import random as rd
    Value=[]
    for i in range(n):
        Value.append(rd.random()*5)
    return Value

def volt_a_Temp_ECT(voltaje):
    """convierte los valores de voltaje a temperatura de un sensor ECT
    Args:
        voltaje (float): valores de voltaje en enteros

    Returns:
        float: _description_
    """
    temp=2*voltaje+10
    return temp

def volt_a_Temp_w1(voltaje):
    """convierte los valores de voltaje a temperatura de un sensor w1
    Args:
        voltaje (float): valores de voltaje en enteros

    Returns:
        float: _description_
    """
    temp=0.1*voltaje+0.24
    return temp

