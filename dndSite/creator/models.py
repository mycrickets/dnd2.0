from django.db import models

# Create your models here.


class Character(models.Model):
    chr_name = models.CharField(max_length=50)
    level = models.IntegerField(default=1)
    player_name = models.CharField(max_length=50)

    def __str(self):
        return self.chr_name
