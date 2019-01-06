import pytest
from api.models.ireportermodels import BaseUser, User, BaseIncident, Incident, IreporterDb
from api import app
from flask import request
import json

class TestUsers(pytest.TestCase):
    def setUp(self):
        self.test_client = app.test_client(self)

    def test_create_user(self):
        user = User(BaseUser("of", "edward", "123456789", "06-jan-2019"),
        2, "edward", "arocha", "arochaedward2018@gmail.com", False)
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'user created successfully')

    def test_user_empty_fields(self):
        user = User(BaseUser("", "", "123456789", "06-jan-2019"),
        2, "edward", "arocha", "arochaedward2018@gmail.com", False)
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'please fill all fields')

    def test_for_valid_email(self):
        user = User(BaseUser("edward", "of", "123456789", "06-jan-2019"),
        2, "edward", "arocha", "arochedward2018@gmail.com", False)
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'invalid email adress')

    def test_check_password_length(self):
        user = User(BaseUser("edward", "of", "123456", "06-jan-2019"),
        2, "edward", "arocha", "arochaedward2018@gmail.com", False)
        user_data = user.make_json()
        response = self.test_client.post(
            'api/v1/users',
            content_type='application/json',
            data=json.dumps(user_data)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(message['message'],
                         'password should be more than 8 characters')     