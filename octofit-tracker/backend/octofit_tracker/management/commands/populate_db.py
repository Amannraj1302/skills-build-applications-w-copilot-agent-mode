from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create users
        tony = User.objects.create(email='tony@marvel.com', name='Tony Stark', team='marvel')
        steve = User.objects.create(email='steve@marvel.com', name='Steve Rogers', team='marvel')
        bruce = User.objects.create(email='bruce@dc.com', name='Bruce Wayne', team='dc')
        clark = User.objects.create(email='clark@dc.com', name='Clark Kent', team='dc')

        # Create workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='easy')
        squats = Workout.objects.create(name='Squats', description='Lower body', difficulty='medium')

        # Create activities
        Activity.objects.create(user=tony, type='run', duration=30, date=date(2024, 1, 1))
        Activity.objects.create(user=steve, type='cycle', duration=45, date=date(2024, 1, 2))
        Activity.objects.create(user=bruce, type='swim', duration=60, date=date(2024, 1, 3))
        Activity.objects.create(user=clark, type='fly', duration=120, date=date(2024, 1, 4))

        # Create leaderboard
        Leaderboard.objects.create(user=tony, score=200, rank=1)
        Leaderboard.objects.create(user=steve, score=180, rank=2)
        Leaderboard.objects.create(user=bruce, score=170, rank=3)
        Leaderboard.objects.create(user=clark, score=160, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
