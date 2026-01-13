from django.core.management.base import BaseCommand
from djongo import models
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        app_models.User.objects.all().delete()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()

        # Create teams
        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        # Create users
        ironman = app_models.User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = app_models.User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = app_models.User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = app_models.User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        app_models.Activity.objects.create(user=ironman, type='Run', duration=30)
        app_models.Activity.objects.create(user=captain, type='Swim', duration=45)
        app_models.Activity.objects.create(user=batman, type='Bike', duration=60)
        app_models.Activity.objects.create(user=superman, type='Yoga', duration=20)

        # Create workouts
        app_models.Workout.objects.create(user=ironman, description='Chest day', calories=500)
        app_models.Workout.objects.create(user=batman, description='Leg day', calories=600)

        # Create leaderboard
        app_models.Leaderboard.objects.create(team=marvel, points=1000)
        app_models.Leaderboard.objects.create(team=dc, points=900)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))