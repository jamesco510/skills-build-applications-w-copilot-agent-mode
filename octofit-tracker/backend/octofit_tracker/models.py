from djongo import models
from bson import ObjectId

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default='', editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(ObjectId())  # Generate a string-based ObjectId
        super().save(*args, **kwargs)

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default='', editable=False)
    name = models.CharField(max_length=255)
    members = models.JSONField(default=list)  # Store user IDs as a list of strings

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(ObjectId())  # Generate a string-based ObjectId
        super().save(*args, **kwargs)

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default='', editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = str(ObjectId())  # Generate a string-based ObjectId
        super().save(*args, **kwargs)

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()