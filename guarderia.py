from boa_constrictor import BoaConstrictor
from ferret import Ferret

class Guarderia:
    def __init__(self):
        # Inicializa dos boas y dos hurones
        self.boa1 = BoaConstrictor("Boa1", 45.5, 5, "Colombia", 40.0)
        self.boa2 = BoaConstrictor("Boa2", 50.0, 6, "Brasil", 30.0)
        self.ferret1 = Ferret("Ferret1", 5.0, 2, "Peru", 5.0)
        self.ferret2 = Ferret("Ferret2", 6.0, 3, "Argentina", 6.0)

    def alimentar_boa(self, boa):
        # Verifica si la boa es None
        if boa is None:
            return "Esta Boa no existe!"

        try:
            # Intenta alimentar a la boa
            boa.eat_mouse()
            return "Éxito"
        except ValueError:
            # Si la boa está llena
            return "La boa está llena"
