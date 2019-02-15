party_list = []


class Party:
    def __init__(self, data=None, party_id=0):
        self.party_list = party_list
        self.data = data
        self.party_id = party_id

    def get_party_list(self):
        return self.party_list

    def get_party(self):
        party_id = int(self.party_id)
        retrieve_party = party_list[party_id - 1]
        return retrieve_party

    def add_party(self):
        if len(party_list) < 1:
            self.party_id = 1
        else:
            self.party_id = len(party_list) + 1
        party_name = self.data["name"]
        logo_url = self.data["logoUrl"]
        party_address = self.data["hqAddress"]
        if len(self.data) == 3:
            new_party = {"name": party_name, "party_id": self.party_id, "logoUrl": logo_url, "hqAddress": party_address}
            party_list.append(new_party)
            return new_party

    def edit_party(self):
        party_id = self.party_id
        new_party_name = self.data["name"]
        for party in party_list:
            if party_id == self.party_id:
                party["name"] = new_party_name
            return new_party_name

    def delete_party(self):
        if len(party_list) > 0:
            for party in party_list:
                if party['party_id'] == int(self.party_id):
                    party_list.remove(party)
                    return "Success"
