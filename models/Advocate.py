from models import Employee, Services


class Advocate(Employee):
    def __init__(self, _full_name: str, _sex: str, _age: int, _services: Services,
                 _price_of_one_service: int, _years_of_experience: int, _salary: int, skills: list,
                 __won_court_proceedings_amount: int, __conducted_proceedings_amount: int, __recommendations_amount):
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
        self.__won_court_proceedings_amount = __won_court_proceedings_amount
        self.__conducted_proceedings_amount = __conducted_proceedings_amount
        self.__recommendations_amount = __recommendations_amount

    def __str__(self):
        return f"Full name: {self._full_name}\nSex: {self._sex}\nAge: {self._age}\nServices: {self._services}\n" \
               f"Price of one service: {self._price_of_one_service}\nYears or experience: {self._years_of_experience}" \
               f"\nSalary: {self._salary}\n Skills: {self._skills}\nWon court proceedings amount: " \
               f"{self.__won_court_proceedings_amount}\n Conducted proceedings amount: " \
               f"{self.__conducted_proceedings_amount}\nRecommendations amount: {self.__recommendations_amount}"
