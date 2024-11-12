from abc import abstractmethod
from animal import Animal

class ExoticAnimal(Animal):
    """
    Esta clase representa a un animal.

    Atributos:
        name (str): Nombre del perro.
        weight (float): Peso del perro en decimales.
        age (int): Edad del perro.
    """

    #Constructor
    def __init__(self, name:str, weight:float, age:int, country:str, taxes:float) -> None:
        super().__init__(name, weight, age)
        self.country = country
        self.taxes = taxes

    #Methods
    @abstractmethod
    def do_sound(self) -> str:
        pass

    def calculate_freight(self) -> float:
        return self.taxes * self.weight

    # Getters y Setters
    @property
    def country(self) -> str:
        """ Devuelve el valor del atributo privado 'country' """
        return self._country
    
    @country.setter
    def country(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'country'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self._country = value
        else:
            raise ValueError('Expected str')
        
    @property
    def taxes(self) -> float:
        """ Devuelve el valor del atributo privado 'taxes' """
        return self._taxes
    
    @taxes.setter
    def taxes(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'taxes'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self._taxes = value
        else:
            raise ValueError('Expected float')