from django.db import models


class Game(models.Model):
    id = models.IntegerField(
        ('Stream ID'),
        help_text=("Id da Steam"),
        primary_key=True
    )
    name = models.CharField(
        ('Name'),
        help_text=("Name of game"),
        max_length=100,
        null=True
    )
    positive_reviews_steam = models.IntegerField(
        ('Positives reviews'),
        help_text=("Number of positives reviews in the game"),
        null=True
    )
    negative_reviews_steam = models.IntegerField(
        ('Negatives reviews'),
        help_text=("Number of negatives reviews in the game"),
        null=True
    )
    owners = models.IntegerField(
        ('Owners'),
        help_text=("Number of owners"),
        null=True
    )
    average_forever = models.IntegerField(
        ('Average forever'),
        help_text=("Average forever of the game"),
        null=True
    )
    average_2weeks = models.IntegerField(
        ('Average 2 weeks'),
        help_text=("Average forever of the game"),
        null=True
    )
    price = models.IntegerField(
        ('Price'),
        help_text=("Price of the game"),
        null=True
    )
    lenguages = models.CharField(
        ('Languages'),
        help_text=("Languages of the game"),
        max_length=100,
        null=True
    )

    def __str__(self):
        """
            Returns the object as a string, the attribute that will represent
            the object.
        """
        return self.name
