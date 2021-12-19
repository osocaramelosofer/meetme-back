from django.db import models


class Quiz(models.Model):

    PREFER_DAY_CHOICES = [
        ('D', 'day'),
        ('N', 'night')
    ]

    DAYS_CHOICES = [
        # Value & readable-name
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday')
    ]

    class COLORS(models.TextChoices):
        BLUE = 'blue'
        RED = 'red'
        PINK = 'pink'
        ORANGE = 'orange'
        BLACK = 'black'
        WHITE = 'white',
        PURPLE = 'purple'
        GREEN = 'green'
        YELLOW = 'yellow'

    owner = models.CharField(max_length=255, blank=True, null=True)

    day_or_night = models.CharField(max_length=2,
                                    choices=PREFER_DAY_CHOICES,
                                    default='N',
                                    blank=True,
                                    null=True)

    favorite_day = models.CharField(max_length=25,
                                    choices=DAYS_CHOICES,
                                    default='friday',
                                    blank=True,
                                    null=True)

    favorite_color = models.CharField(max_length=255,
                                      choices=COLORS.choices,
                                      blank=True,
                                      null=True)

    def __str__(self):
        return f"Quiz # {self.owner}"
