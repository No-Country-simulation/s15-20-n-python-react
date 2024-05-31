from rest_framework.test import APITestCase

# Create your tests here.


class TestUser(APITestCase):
    def setUp(self):
        self.client.post(
            '/user/list/', {'username': 'test', 'password': 'testpassword', 'email': 'test@test.com'}, format='json')

    def test_get_users_api(self):
        request = self.client.get('/user/list/')
        self.assertEqual(request.status_code, 200)

    def test_create_user_api(self):
        request = self.client.post(
            '/user/list/', {'username': 'test2', 'password': 'testpassword', 'email': 'test2@test.com'}, format='json')
        self.assertEqual(request.status_code, 201)

    def test_update_user_api(self):
        request = self.client.put(
            '/user/detail/1/', {'username': 'tester', 'password': 'testerPassword', 'email': 'test@test.net'}, format='json')
        self.assertEqual(request.status_code, 200)

    def test_delete_user_api(self):
        request = self.client.delete('/user/detail/1/')
        self.assertEqual(request.status_code, 204)
