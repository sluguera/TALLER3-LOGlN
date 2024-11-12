from exotic_animal import ExoticAnimal

class Ferret(ExoticAnimal):
    def __init__(self, name: str, weight: float, age: int, country: str, taxes: float) -> None:
        super().__init__(name, weight, age, country, taxes)

    @staticmethod
    def do_sound() -> str:
        return "¡Eek Eek!"