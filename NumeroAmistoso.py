num1 = int(input("ingresa el primer numero: "))
num2 = int(input("ingresa el segundo numero: "))

def suma_divisores_propios(n):
    suma = 0
    for i in range(1, n // 2 + 1): 
        if n % i == 0:
            suma += i
    return suma

def son_numeros_amistosos(a, b):
    suma_a = suma_divisores_propios(a)
    suma_b = suma_divisores_propios(b)
    return suma_a == b and suma_b == a

# Ejemplo de uso

if son_numeros_amistosos(num1, num2):
    print(f"{num1} y {num2} son números amistosos.")
else:
    print(f"{num1} y {num2} no son números amistosos.")