from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from .validators import (
    # MaxLengthClassValidator,
    TextContainsOnlyAlphaNumericAndUnderscoreValidator,
    CustomFloatPositiveValidator
)

# Create your models here.
"""
Profile
o Username
    ▪ Character field, required.
    ▪ It should have at least 2 characters and maximum - 15 characters.
    ▪ The username can consist only of letters, numbers, and underscore ("_"). 
    Otherwise, raise a ValidationError with the message: "Ensure this value contains only letters,
    numbers, and underscore."
o Email
    ▪ Email field, required.
o Age
    ▪ Integer field, optional.
    ▪ The age cannot be below 0
"""


class Profile(models.Model):
    username = models.CharField(
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            #MaxLengthClassValidator(15),
            MaxLengthValidator(15),
            TextContainsOnlyAlphaNumericAndUnderscoreValidator()
        ]
    )
    email = models.EmailField(blank=False, null=False)
    age = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username


"""
Album Name
    ▪ Character field, required.
    ▪ All album names must be unique.
    ▪ It should consist of a maximum of 30 characters.
o Artist
    ▪ Character field, required.
    ▪ It should consist of a maximum of 30 characters.
    
o Genre
    ▪ Char field, required.
    ▪ It should consist of a maximum of 30 characters.
    ▪ The choices are "Pop Music", "Jazz Music", "R&B Music", "Rock Music",
    "Country Music", "Dance Music", "Hip Hop Music", and "Other".
o Description
    ▪ Text field, optional.
o Image URL
    ▪ URL field, required.
o Price
    ▪ Float field, required.
    ▪ The number of decimal places of the price should not be specified in the database.
    ▪ The price cannot be below 0.0
"""


class Album(models.Model):
    GENRE_CHOICES = [
        ("pop", "Pop Music"),
        ("jazz", "Jazz Music"),
        ("rnb", "R&B Music"),
        ("rock", "Rock Music"),
        ("country", "Country Music"),
        ("dance", "Dance Music"),
        ("hiphop", "Hip Hop Music"),
        ("other", "Other")
    ]

    album_name = models.CharField(
        blank=False, null=False, max_length=30, unique=True
    )
    artist = models.CharField(
        blank=False, null=False, max_length=30
    )
    genre = models.CharField(
        blank=False, null=False,
        max_length=30, choices=GENRE_CHOICES
    )

    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=False, null=False)
    price = models.FloatField(
        blank=False, null=False,
        validators=[CustomFloatPositiveValidator()]
    )
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
