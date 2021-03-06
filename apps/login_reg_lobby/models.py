from django.db import models
import re

class PlayerManager(models.Manager):
    def validator(self, post_data):
        errors = {}
        if len(post_data['name']) == 0:
            errors['name'] = "You must enter a name!"
        return errors

class Player(models.Model):
    name = models.CharField(max_length = 45)
    vic_points = models.IntegerField(default=0)
    wheat = models.IntegerField(default=0)
    ore = models.IntegerField(default=0)
    brick = models.IntegerField(default=0)
    lumber = models.IntegerField(default=0)
    sheep = models.IntegerField(default=0)
    objects = PlayerManager()