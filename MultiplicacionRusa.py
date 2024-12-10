def multiplicacion_rusa(a, b):
    resultado = 0
    while b > 0:
        if b % 2 != 0: 
            resultado += a
        a *= 2  
        b //= 2 
    return resultado


# ejemplos de uso 
numero1 = 25
numero2 = 12

resultado = multiplicacion_rusa (numero1, numero2)
print (f"el resultado de multiplicar {numero1} y {numero2} es: {resultado}")
