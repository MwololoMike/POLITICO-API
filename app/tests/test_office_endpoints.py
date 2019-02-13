from unittest import TestCase
from run import app
import json


class TestOfficesEndpoints(TestCase):
    def setUp(self):
        self.politico_client = app.test_client()

    def tearDown(self):
        self.politico_client.get("/delete")

    def test_admin_create_office_successfully(self):
        response = self.politico_client.post("/offices", data=json.dumps({
            "name": "office_name",
            "type": "office_type"
        }))
        self.assertTrue(response.status_code == 201)
        self.assertTrue(response.json['data'][0]['office_id'] == 1)

    def test_admin_create_office_failed(self):
        response = self.politico_client.post("/offices", data=json.dumps({
            "name": "office_name",
            "id": "office_type"
        }))
        self.assertTrue(response.status_code == 400)
        self.assertTrue(response.json['message'] == "Unable to create office")

    def test_get_all_offices_successfully(self):
        self.politico_client.post("/offices", data=json.dumps({
            "name": "party_name",
            "type": "office_type"
        }))
        response = self.politico_client.get("/offices", data=json.dumps({
        }))
        self.assertTrue(response.status_code == 200)

    def test_get_all_offices_failed(self):
        self.politico_client.post("/offices", data=json.dumps({
            "name": "party_name",
            "type": "office_type"
        }))
        response = self.politico_client.get("/offies", data=json.dumps({
        }))
        self.assertTrue(response.status_code == 404)
