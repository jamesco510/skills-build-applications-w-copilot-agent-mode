from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users with explicit string IDs
        user1 = User.objects.create(id="user1", email="john.doe@example.com", name="John Doe")
        user2 = User.objects.create(id="user2", email="jane.smith@example.com", name="Jane Smith")

        # Create test teams
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")

        # Add users to teams
        team1.members.append(str(user1.id))
        team2.members.append(str(user2.id))
        team1.save()
        team2.save()

        # Create test activities
        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(team=team1, score=100)
        Leaderboard.objects.create(team=team2, score=150)

        # Create test workouts
        Workout.objects.create(name="Morning Yoga", description="A relaxing yoga session to start the day.")
        Workout.objects.create(name="HIIT Training", description="High-intensity interval training for advanced users.")

        # Additional test data for diversity
        user3 = User.objects.create(id="user3", email="alex.jones@example.com", name="Alex Jones")
        team3 = Team.objects.create(name="Team Gamma")
        team3.members.append(str(user3.id))
        team3.save()

        Activity.objects.create(user=user3, type="Swimming", duration=60)
        Leaderboard.objects.create(team=team3, score=200)
        Workout.objects.create(name="Evening Stretch", description="A calming stretch routine to end the day.")

        self.stdout.write(self.style.SUCCESS('Test data successfully populated.'))