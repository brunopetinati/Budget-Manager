from django.test import TestCase
from rest_framework.test import APIClient


class TestAccountView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.create_user = { 
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

        self.user_login = {
	    "email":"userlastname@email.com",
	    "password":"1234"
        }

    def test_create_and_login_for_user_account(self):
        # create user
        user = self.client.post(
            "/api/accounts/", self.create_user, format="json"
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
            "/api/login/", self.user_login, format="json"
        ).json()

        self.assertIn("token", response.keys())

class TestInfrastructureView(TestCase):
    def setUp(self):

        self.create_user = { 
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

        self.user_login = {
	    "email":"userlastname@email.com",
	    "password":"1234"
        }

        self.transaction_data_credit = {
        "description":"Teste",
        "transaction_type":"credit",
        "amount": "20.00"
    }

        self.transaction_data_debt = {
        "description":"Teste",
        "transaction_type":"debt",
        "amount": "10.00"
    }

    def test_admin_create_transaction_credit(self):
        client = APIClient()

        user = client.post("/api/accounts/", self.create_user, format="json").json()

        token = client.post("/api/login/", self.user_login, format="json").json()[
            "token"
        ]

        client.credentials(HTTP_AUTHORIZATION="Token " + token)

        transaction_credit = client.post("/api/transactions/", self.transaction_data_credit, format="json").json()


        self.assertEqual(transaction_credit["id"], 1)
        self.assertEqual(transaction_credit["transaction_type"], "credit")
        self.assertEqual(transaction_credit["amount"], '20.00')

    def test_admin_create_transaction_debt(self):

        client = APIClient()

        user = client.post("/api/accounts/", self.create_user, format="json").json()

        token = client.post("/api/login/", self.user_login, format="json").json()[
            "token"
        ]

        client.credentials(HTTP_AUTHORIZATION="Token " + token)

        transaction_debt = client.post("/api/transactions/", self.transaction_data_debt, format="json").json()

        self.assertEqual(transaction_debt["id"], 1)
        self.assertEqual(transaction_debt["transaction_type"], "debt")
        self.assertEqual(transaction_debt["amount"], '10.00')


