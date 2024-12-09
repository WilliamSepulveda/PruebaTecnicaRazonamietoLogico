def fibonacci(n):
    if n == 0: 
        return "el numero debe ser mayor a 1."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

numero = int(input("introduce el numero entero: "))
resultado = fibonacci(numero)

print (f"El {numero} numero de Fibonacci es : {resultado}")