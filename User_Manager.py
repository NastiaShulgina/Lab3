from Advocate import Advocate
from User import Services
class UserManager():
    def __init__(self, court_list: list):
        self.court_list = court_list

    def search_by_services_and_sort_by_names(self, skill, order):
        out = list()
        for service in self.court_list:
            if service._skills == skill:
                out.append(service)
            self.court_list = out
        self.court_list.sort(key=lambda x: x._full_name.lower(), reverse=order)
        return self.court_list

    def sort_by_price(self, order):
        self.court_list.sort(key=lambda x: x._price_of_one_service, reverse = order)
        return self.court_list
a = Advocate("Petro Petrenko", "Male", 50, Services.COURT_PROCEEDINGS, 12000, 20, 90000, Services.COURT_PROCEEDINGS,
              5, 6, 7)
b = Advocate("Iryna Irynenko", "Male", 50, Services.COURT_PROCEEDINGS, 4000, 20, 90000, Services.COURT_PROCEEDINGS,
              5, 6, 7)
c = Advocate("Detro Detrenko", "Male", 50, Services.COURT_PROCEEDINGS, 7000, 20, 90000, Services.COURT_PROCEEDINGS,
              5, 6, 7)
d = Advocate("Detro Detrenko", "Male", 50, Services.CONSULTATION, 10000, 20, 90000, Services.COPYRIGHT_REGISTRATION_AND_PROTECTION,
              5, 6, 7)
all_objects = [a, b, c, d]
manager_object = UserManager (all_objects)
out = manager_object.search_by_services_and_sort_by_names(Services.COURT_PROCEEDINGS, False)
#for i in out:
#    print (i)

out1 = manager_object.sort_by_price(False)
for i in out1:
    print(i)  