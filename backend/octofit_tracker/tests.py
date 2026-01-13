from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        Activity.objects.create(user=ironman, type='Run', duration=30)
        Workout.objects.create(user=batman, description='Leg day', calories=600)
        Leaderboard.objects.create(team=marvel, points=1000)

    def test_user_team(self):
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Team.objects.count(), 2)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
