from django.test import TestCase
from core.models import Team

# Create your tests here.


class TeamListViewTests(TestCase):

    def setUp(self):
        Team.objects.create(name='Team 1')

    def test_team_list_returns_200(self):
        request = self.client.get('/team/team/list/')
        self.assertEqual(request.status_code, 200)

    def test_team_create_returns_200(self):
        request = self.client.post('/team/team/list/', data={'name': 'Team 2'})
        self.assertEqual(request.status_code, 200)
        team = Team.objects.filter(name='Team 2').first()
        self.assertIsNotNone(team)
