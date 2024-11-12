from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def eat(self, kg) -> None:
        pass

    @abstractmethod
    def get_kilograms_eaten() -> float:
        pass