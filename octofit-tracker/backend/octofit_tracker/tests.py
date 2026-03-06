from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test', email='test@example.com', team='Marvel')
        self.assertEqual(user.name, 'Test')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel', members=['test@example.com'])
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user_email='test@example.com', activity='Run', duration=30)
        self.assertEqual(activity.activity, 'Run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(user_email='test@example.com', score=100)
        self.assertEqual(lb.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(user_email='test@example.com', workout='Pushups', reps=20)
        self.assertEqual(workout.workout, 'Pushups')
