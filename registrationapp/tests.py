from django.test import TestCase , Client
from django.urls import reverse
from registrationapp.models import Company, User
# from store.logic import operations

# Create your tests here.

# class TestUrls(TestCase):
    # Перевіряємо чи доступна сторінка чи ні 
        # def test_homepage_url(self):
        #     response = self.client.get(reverse('main'))
        #     self.assertEqual(response.status_code, 200)

        # @classmethod
        # def setUpClass(cls):
        #     super().setUpClass()
        #     # Підготовка тестових даних
        #     Company.objects.create(name='Test Company', employee='John Doe')

        # def test_name_field(self):
        #     company = Company.objects.get(id=1)
        #     field_label = company._meta.get_field('name').verbose_name
        #     self.assertEquals(field_label, 'name')

        # def setUp(self):
        #     self.client = Client()
        #     self.username = 'testuser'
        #     self.password = 'testpassword'
        #     self.user = User.objects.create_user(username=self.username, password=self.password)

        # def test_user_login(self):
        #     response = self.client.post('/', {'username': self.username, 'password': self.password})
        #     self.assertEqual(response.status_code, 200)
        #     self.assertTrue(response.context['user'].is_authenticated)

        # def test_invalid_user_login(self):
        #     response = self.client.post('/', {'username': 'invaliduser', 'password': 'invalidpassword'})
        #     self.assertEqual(response.status_code, 200)
        #     self.assertFalse(response.context['user'].is_authenticated)    