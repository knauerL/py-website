from django.db import models

# Create your models here.

class player(models.Model):
    plName = models.CharField(max_length=40, default="", help_text="Your name")