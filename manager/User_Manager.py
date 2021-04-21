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
        self.court_list.sort(key=lambda x: x._price_of_one_service, reverse=order)
        return self.court_list
