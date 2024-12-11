def findLongestSubsequence(arr):
    arr.sort()

    current_sum = 0
    max_length = 0

    for i in range(len(arr)):
        current_sum += arr[i]  

        if current_sum % 2 == 0:
            max_length = i + 1

    return max_length

# Ejemplo de uso:
n = int(input("Introduce el número de elementos: "))
arr = []
for _ in range(n):
    arr.append(int(input()))

resultado = findLongestSubsequence(arr)
print("La longitud de la subsecuencia más larga es:", resultado)
