from unittest import TestCase
from run import app
import json


class TestPartiesEndpoints(TestCase):
    def setUp(self):
        self.politico_client = app.test_client()

    def tearDown(self):
        self.politico_client.get("/delete")

    def test_admin_create_party_successfully(self):
        response = self.politico_client.post("/parties", data=json.dumps({
            "name": "party_name",
            "logoUrl": "logo_url",
            "hqAddress": "party_address"
        }))
        self.assertTrue(response.status_code == 201)
        self.assertTrue(response.json['data'][0]['party_id'] == 1)

    def test_admin_create_party_failed(self):
        response = self.politico_client.post("/parties", data=json.dumps({
            "name": "party_name",
            "logoUrl": "logo_url"
        }))
        self.assertTrue(response.status_code == 400)
        self.assertTrue(response.json['message'] == "Please enter valid data to create party.")

    def test_admin_edit_party_successfully(self):
        self.politico_client.post("/parties", data=json.dumps({
            "name": "party_name",
            "logoUrl": "logo_url",
            "hqAddress": "party_address"
        }))
        response = self.politico_client.patch("/parties/1/name", data=json.dumps({
            "name": "new_party_name"
        }))
        self.assertTrue(response.status_code == 202)
        self.assertTrue(response.json['message'] == "Party name updated successfully")

    def test_admin_edit_party_failed(self):
        response = self.politico_client.patch("/parties/99/name", data=json.dumps({
            "name": "new_party_name"
        }))
        self.assertTrue(response.status_code == 404)
        self.assertTrue(response.json['message'] == "Unable to update party.")

    def test_get_all_parties_success(self):
        self.politico_client.post("/parties", data=json.dumps({
            "name": "party_name",
            "logoUrl": "logo_url",
            "hqAddress": "party_address"
        }))
        response = self.politico_client.get("/parties")
        self.assertTrue(response.status_code == 200)

    def test_get_all_parties_failed(self):
        self.politico_client.post("/parties", data=json.dumps({
            "name": "party_name",
            "logoUrl": "logo_url",
            "hqAddress": "party_address"
        }))
        response = self.politico_client.get("/partiies")
        self.assertTrue(response.status_code == 404)

    def test_admin_delete_party_success(self):
        self.politico_client.post("/parties", data=json.dumps({
            "name": "party_name",
            "logoUrl": "logo_url",
            "hqAddress": "party_address"
        }))
        response = self.politico_client.delete("/parties/1")
        self.assertEqual(response.status_code, 200)

    def test_admin_delete_party_fail(self):
        self.politico_client.post("/parties", data=json.dumps({
            "name": "party_name",
            "logoUrl": "logo_url",
            "hqAddress": "party_address"
        }))
        response = self.politico_client.delete("/parties/69")
        self.assertTrue(response.status_code == 404)
