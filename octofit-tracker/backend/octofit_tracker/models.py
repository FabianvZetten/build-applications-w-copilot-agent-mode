from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    members = models.JSONField(default=list)
    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user_email = models.EmailField()
    activity = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.activity}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user_email = models.EmailField()
    score = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user_email = models.EmailField()
    workout = models.CharField(max_length=100)
    reps = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.workout}"