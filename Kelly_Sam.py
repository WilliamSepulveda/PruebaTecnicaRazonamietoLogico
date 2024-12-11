def dias_minimos_para_superar(samDiario, kellyDiario, diferencia):
    if kellyDiario <= samDiario:
        return -1
    
    # Calcular el número de días necesarios
    dias = (diferencia // (kellyDiario - samDiario)) + 1 if diferencia > 0 else 1
    return dias

# Ejemplo de uso
samDiario = 3
kellyDiario = 5
diferencia = 5

resultado = dias_minimos_para_superar(samDiario, kellyDiario, diferencia)
print(f"El número mínimo de días para que Kelly supere a Sam es: {resultado}")
