def generar_fibonacci(hasta):
    secuencia = [0, 1]
    while secuencia[-1] < hasta:
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia


def pertenence_a_fibonacci(numero):
    secuencia = generar_fibonacci(numero)
    return numero in secuencia

numero = int(input("ingrese el numero a validar: "))
if pertenence_a_fibonacci(numero):
    print(f"{numero} es un numero de Fibonacci")
else:
    print(f"{numero} no es un numero de Fibonacci")