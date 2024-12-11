class VotacionCONFECH:
    def __init__(self, num_universidades):
        self.num_universidades = num_universidades
        self.universidades = []
        self.resultados = {"A": 0, "R": 0, "N": 0, "B": 0}

    def registrar_universidad(self, nombre, votos):
        votos_validos = {"A": 0, "R": 0, "N": 0, "B": 0}
        for voto in votos:
            if voto in votos_validos:
                votos_validos[voto] += 1
                self.resultados[voto] += 1
            else:
                print(f"Voto inválido '{voto}' ignorado.")
        self.universidades.append({"nombre": nombre, "votos": votos_validos})

    def mostrar_resultados_por_universidad(self):
        print("\nResultados por universidad:")
        for uni in self.universidades:
            nombre = uni["nombre"]
            votos = uni["votos"]
            print(f"{nombre}: Aceptar (A): {votos['A']}, Rechazar (R): {votos['R']}, Nulo (N): {votos['N']}, Blanco (B): {votos['B']}")

    def mostrar_resultados_totales(self):
        print("\nResultados totales:")
        print(f"Aceptar (A): {self.resultados['A']}")
        print(f"Rechazar (R): {self.resultados['R']}")
        print(f"Nulo (N): {self.resultados['N']}")
        print(f"Blanco (B): {self.resultados['B']}")

        if self.resultados['A'] > self.resultados['R']:
            print("Resultado final: Aceptar (A)")
        elif self.resultados['A'] < self.resultados['R']:
            print("Resultado final: Rechazar (R)")
        else:
            print("Resultado final: Empate entre Aceptar (A) y Rechazar (R)")

# Ejemplo de uso
if __name__ == "__main__":
    print("Bienvenido al sistema de votación de la CONFECH\n")

    while True:
        try:
            num_universidades = int(input("Ingresa la cantidad de universidades que participan en el proceso: "))
            if num_universidades > 0:
                break
            else:
                print("El número de universidades debe ser mayor a 0. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

    votacion = VotacionCONFECH(num_universidades)

    for i in range(num_universidades):
        nombre = input(f"Ingresa el nombre de la universidad #{i + 1}: ")
        votos = []
        print("Ingresa los votos (A para aceptar, R para rechazar, N para nulo, B para blanco). Finaliza con 'X':")
        while True:
            voto = input("Voto: ").upper()
            if voto == "X":
                break
            votos.append(voto)
        votacion.registrar_universidad(nombre, votos)

    votacion.mostrar_resultados_por_universidad()
    votacion.mostrar_resultados_totales()
