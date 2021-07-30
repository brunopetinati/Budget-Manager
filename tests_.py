from django.test import TestCase
from rest_framework.test import APIClient


class TestAccountView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.create_user_1 = { 
        "username": "user1",
        "first_name":"User", 
        "last_name":"Last Name", 
        "full_name":"User Last Name",
        "email":"userlastname@email.com",
        "date_of_birth":"1990-12-12",
        "CPF":"35555555555",
        "wallet": 100,
        "password":"1234"
        }

        self.user1_login = {
	    "email":"userlastname@email.com",
	    "password":"1234"
        }

    def test_create_and_login_for_user_account(self):
        # create user
        user = self.client.post(
            "/api/accounts/", self.create_user_1, format="json"
        )

        # testa se o user foi criado corretamente
        self.assertEqual(
            user.json(), {
            "id":1, 
            "username": "user1",
            "first_name":"User", 
            "last_name":"Last Name", 
            "full_name":"User Last Name",
            "email":"userlastname@email.com",
            "phone_number":None,
            "date_of_birth":"1990-12-12",
            "CPF":"35555555555",
            "wallet": 100,
        }
        )
        self.assertEqual(user.status_code, 201)

        # testa se o login foi realizado corretamente e se o token é retornado
        response = self.client.post(
            "/api/login/", self.user1_login, format="json"
        ).json()

        self.assertIn("token", response.keys())
