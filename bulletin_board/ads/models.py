from django.contrib.auth.models import User
from django.db import models


class Ads(models.Model):
    TYPE = [
        ('TK', 'Tank'),
        ('HL', 'Healer'),
        ('DD', 'Damage dealer'),
        ('TR', 'Trader'),
        ('GM', 'Guild master'),
        ('QG', 'Quest giver'),
        ('WS', 'Warsmith'),
        ('TN', 'Tanner'),
        ('PM', 'Potion maker'),
        ('SM', 'Spell master'),
    ]
    header = models.CharField(max_length=128)
    text = models.TextField()
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=TYPE, default='TK')


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    text = models.TextField()
