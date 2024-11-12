from guarderia import Guarderia

if __name__ == "__main__":
    guarderia = Guarderia()

    # Prueba 1: Alimentar una boa normalmente
    print(guarderia.alimentar_boa(guarderia.boa1))  # Debería imprimir "Éxito"

    # Prueba 2: Alimentar una boa hasta el límite y luego intentar de nuevo
    for _ in range(10):
        guarderia.alimentar_boa(guarderia.boa1)
    print(guarderia.alimentar_boa(guarderia.boa1))  # Debería imprimir "La boa está llena"

    # Prueba 3: Pasar None como parámetro
    print(guarderia.alimentar_boa(None))  # Debería imprimir "Esta Boa no existe!"
