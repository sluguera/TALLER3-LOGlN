from exotic_animal import ExoticAnimal

class BoaConstrictor(ExoticAnimal):
    mouse_weight:float = 1.5

    def __init__(self, name: str, weight: float, age: int, country: str, taxes: float) -> None:
        super().__init__(name, weight, age, country, taxes)
        self._eaten_mice = 0  # Cambiado de __eaten_mice a _eaten_mice

    @staticmethod
    def do_sound() -> str:
        return "¡Tsss!"

    def eat_mouse(self, amount=1) -> None:
        if self._eaten_mice + amount > 10:
            raise ValueError("Demasiados Ratones!")
        self._eaten_mice += amount
        self.eat(self.mouse_weight * amount)

    @property
    def eaten_mice(self) -> int:
        """ Devuelve el número de ratones comidos """
        return self._eaten_mice

    def calculate_freight(self) -> float:
        return self.taxes * self.weight

        

