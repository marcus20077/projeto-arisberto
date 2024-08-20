def circulo(tipoC, raio):
    r=0
    if tipoC == "area":
        r= 3.14 + (raio ** 2)
    elif tipoC == "perimetro":
        r= 2 * 3.14 * (raio)
    return r  

ca= circulo("area", 5)
print(f'area: {ca}')
