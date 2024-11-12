from abc import abstractmethod
from ianimal import IAnimal

class Animal(IAnimal):
    """
    Esta clase representa a un animal.

    Atributos:
        name (str): Nombre del perro.
        weight (float): Peso del perro en decimales.
        age (int): Edad del perro.
    """

    #Constructor
    def __init__(self, name:str, weight:float, age:int) -> None:
        self.name = name
        self.weight = weight
        self.age = age
        self._kilograms_eaten = 0

    #Methods
    def eat(self, kg) -> None:
        self._kilograms_eaten += kg
    
    def get_kilograms_eaten(self) -> float:
        return self._kilograms_eaten

    @abstractmethod
    def do_sound(self) -> str:
        pass

    # Getters y Setters
    @property
    def name(self) -> str:
        """ Devuelve el valor del atributo privado 'name' """
        return self._name
    
    @name.setter
    def name(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'name'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('Expected str')
        
    @property
    def weight(self) -> float:
        """ Devuelve el valor del atributo privado 'weight' """
        return self._weight
    
    @weight.setter
    def weight(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'weight'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._weight = value
        else:
            raise ValueError('Expected float')
        
    @property
    def age(self) -> int:
        """ Devuelve el valor del atributo privado 'age' """
        return self._age
    
    @age.setter
    def age(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'age'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self._age = value
        else:
            raise ValueError('Expected int')