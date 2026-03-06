from django.core.management.base import BaseCommand
from django.conf import settings
## removed unnecessary import of djongo.connection
from django.contrib.auth.models import User
from bson import ObjectId

import pymongo

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample data
        users = [
            {"_id": ObjectId(), "name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"_id": ObjectId(), "name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"_id": ObjectId(), "name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"_id": ObjectId(), "name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"_id": ObjectId(), "name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"_id": ObjectId(), "name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        db.users.insert_many(users)

        teams = [
            {"_id": ObjectId(), "name": "DC", "members": [u["email"] for u in users if u["team"] == "DC"]},
            {"_id": ObjectId(), "name": "Marvel", "members": [u["email"] for u in users if u["team"] == "Marvel"]},
        ]
        db.teams.insert_many(teams)

        activities = [
            {"_id": ObjectId(), "user_email": "superman@dc.com", "activity": "Flight", "duration": 60},
            {"_id": ObjectId(), "user_email": "ironman@marvel.com", "activity": "Suit Training", "duration": 45},
        ]
        db.activities.insert_many(activities)

        leaderboard = [
            {"_id": ObjectId(), "user_email": "superman@dc.com", "score": 1000},
            {"_id": ObjectId(), "user_email": "ironman@marvel.com", "score": 950},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"_id": ObjectId(), "user_email": "batman@dc.com", "workout": "Martial Arts", "reps": 100},
            {"_id": ObjectId(), "user_email": "cap@marvel.com", "workout": "Shield Throws", "reps": 50},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
