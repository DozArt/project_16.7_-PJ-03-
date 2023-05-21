from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


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

    def __str__(self):
        return self.header.title()

    def get_absolute_url(self):
        return reverse('ad', args=[str(self.id)])


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('ad', args=[str(self.ads.id)])
