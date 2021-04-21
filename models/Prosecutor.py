from Employee import Employee
from User import Services


class Prosecutor(Employee):
    def __init__(self, _full_name: str, _sex: str, _age: int, _services: Services,
                 _price_of_one_service: int, _years_of_experience: int, _salary: int, skills: list,
                 __corruptibility: bool, __investigation_management: bool):
        super().__init__(_full_name, _sex, _age, _services, _price_of_one_service, _years_of_experience, _salary,
                         skills)
        self._full_name = _full_name
        self._sex = _sex
        self._age = _age
        self._services = _services
        self._price_of_one_service = _price_of_one_service
        self._years_of_experience = _years_of_experience
        self._salary = _salary
        self._skills = skills
        self.__corruptibility = __corruptibility
        self.__investigation_management = __investigation_management

    def __str__(self):
        return f"Full name: {self._full_name}\nSex: {self._sex}\nAge: {self._age}\nServices: {self._services}\n" \
               f"Price of one service: {self._price_of_one_service}\nYears or experience: {self._years_of_experience}" \
               f"\nSalary: {self._salary}\nSkills: {self._skills}\nCorruptibility: {self.__corruptibility}\n" \
               f"Investigation management: {self.__investigation_management}"
