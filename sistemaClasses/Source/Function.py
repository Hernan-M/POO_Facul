class Function:
    def __init__(self, cod: int, name: str):
        self.__name = name
        self.__cod = cod

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cod(self):
        return self.__cod

    @cod.setter
    def cod(self, cod: int):
        self.__cod = cod