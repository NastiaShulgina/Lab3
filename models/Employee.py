from models import User_class, Services


class Employee (User_class):
    def __init__(self, _full_name: str, _sex: str, _age: int, _services: Services,
                 _price_of_one_service: int, _years_of_experience: int, _salary: int, _skills: list):
        super().__init__(_full_name, _sex, _age, _services)
        self._price_of_one_service = _price_of_one_service
        self._years_of_experience = _years_of_experience
        self._salary = _salary
        self._skills = _skills

    def __str__(self):
        return f"Full name: {self._full_name}\nSex: {self._sex}\nAge: {self._age}\nServices: {self._services}\n\
            Price of one service: {self._price_of_one_service}\nYears or experience: {self._years_of_experience}\n" \
               f"Salary: {self._salary}\n\ Skills: {self._skills}"
