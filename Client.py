from User import User, Services
class Client (User):
    def __init__(self, _full_name: str, _sex: str, _age: int, _services: Services,
     __price_limit: int, __needed_services = list):
        super().__init__( _full_name, _sex, _age, _services)
        self.__price_limit = __price_limit
        self.__needed_services = __needed_services

    def __str__(self):
        return f"Full name: {self._full_name}\nSex: {self._sex}\nAge: {self._age}\nServices: {self._services}\n\
        Price limit: {self.__price_limit}\nNeeded services: {self.__needed_services}\n"