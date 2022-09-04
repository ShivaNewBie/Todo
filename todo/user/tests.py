import json

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from user.models import CustomUser

from task.models import Task

from task.api.serializers import TaskSerializer
from django.urls import reverse

# class RegistrationTestCase(APITestCase):
#     def test_registration(self):

#         data = {'username': 'testasdasd','email': 'test@user.com', 'password1': 
#         'testing-this-password', 'password2':'testing-this-password'}
#         response = self.client.post('/accounts/register/',data, format='json') 
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TodoViewSetTestCase(APITestCase):
    list_url = reverse("Task-list")
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='shiva', password='testing_this_password')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
    
    def test_todo_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_todo_list_unauthorized(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_todo_list_get(self):
        test = Task.objects.create(description='test',user=self.user,status=False, slug='django' )
        response = self.client.get(reverse("Task-detail", kwargs={"slug": test.slug }))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "shiva")
    
    def test_todo_list_update_by_owner(self):
        test = Task.objects.create(description='test',user=self.user,status=False, slug='django' )
        response = self.client.put(reverse("Task-detail", kwargs={"slug": 'django'}),
                                   {"description": "test update", "user": test.user, "status": False, "slug":"django"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(json.loads(response.content),
        #                  {"description": "test update", "user": test.user, "status": False, "slug":"django"})