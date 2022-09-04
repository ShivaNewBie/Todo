# import json

# from rest_framework import status
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APITestCase
# from user.models import CustomUser

# from task.api.serializers import TaskSerializer

# class RegistrationTestCase(APITestCase):
#     def test_registration(self):

#         data = {'username': 'test','email': 'test@user.com', 'password1': 
#         'testing_this_password', 'password2':'testing_this_password'}

#         response = self.client.post('/auth/users/',data)

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
