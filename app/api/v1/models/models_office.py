office_list = []


class Office:
    def __init__(self, data=None, office_id=0):
        self.office_list = office_list
        self.data = data
        self.office_id = office_id

    def get_office_list(self):
        return self.office_list

    def get_office(self):
        office_id = int(self.office_id)
        retrieve_office = office_list[office_id]
        return retrieve_office

    def add_office(self):
        if len(office_list) > 0:
            self.office_id = len(office_list) + 1

        else:
            self.office_id = 1

        if len(self.data) == 2:
            office_name = self.data["name"]
            office_type = self.data['type']
            office_id = self.office_id
            new_office = {"name": office_name, "office_id": office_id, "type": office_type}

            office_list.append(new_office)
            return new_office
