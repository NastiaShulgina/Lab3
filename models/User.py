from enum import Enum


class Services(Enum):
    COMPANY_REGISTRATION = 0
    PROVIDING_CONSULTATION = 1
    BUSINESS_PAPERS_PREPARATION = 2
    FIRM_RESALE_GUARANTEE = 3
    ASSISTANCE_IN_REAL_ESTATE_TRANSACTIONS = 4
    APPLICATION_REGISTRATION = 5
    COPYRIGHT_REGISTRATION_AND_PROTECTION = 6
    CONSULTATION = 7
    COURT_PROCEEDINGS = 8


class User_class:
    def __init__(self, _full_name: str, _sex: str, _age: int, _services: Services):
        self._full_name = _full_name
        self._sex = _sex
        self._age = _age 
        self._services = _services

    def __str__(self):
        return f"Full name: {self._full_name}\n Sex: {self._sex}\n Age: {self._age}\n Services: {self._services}"
