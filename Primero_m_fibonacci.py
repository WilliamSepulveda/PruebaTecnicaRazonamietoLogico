m = int(input("Ingresa la cantidad de números de Fibonacci que deseas mostrar: "))

if m <= 0:
    print("Por favor, ingresa un número mayor a 0.")
else:
    fibonacci = [0, 1]

    for i in range(2, m):
        siguiente = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(siguiente)

    print("Los primeros", m, "números de Fibonacci son:")
    print(fibonacci[:m])
