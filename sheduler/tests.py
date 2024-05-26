from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.urls import reverse

class YourTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_exam_schedule(self):
        url = reverse('create_exam_schedule')
        data = {
            'course': 'Your Course',
            'date_time': '2024-04-10T12:00:00',
            'venue': 'Your Venue',
            'supervisors': [], 
            'exam_officer': self.user.id  
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201) 
