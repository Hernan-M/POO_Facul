class Functionary:
    def __init__(self, name: str, cpf: int, function: str, salary: float, tel: int):
        self.__name = name
        self.__cpf = cpf
        self.__function = function
        self.__salary = salary
        self.__tel = tel

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, function: str):
        self.__function = function

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, tel: int):
        self.__tel = tel