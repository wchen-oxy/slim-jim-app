import datetime
from django.db import models
from django.utils import timezone




class Recipe(models.Model):
    RecipeName = models.TextField(default='')
    Servings = models.TextField(default='')
    Calories = models.CharField(max_length=10, default='')
    PrepTime = models.CharField(max_length=10, default='')
    CookTime = models.CharField(max_length=10, default='')
    DietaryRestr = models.TextField(default='')
    Ingredients = models.TextField(default='')
    Instructions = models.TextField(default='')
    Translation = models.TextField(default='')


    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    def __str__(self):
        return self.RecipeName


class Exercise(models.Model):
    Name = models.TextField(default='')
    Location = models.TextField(default='')
    #Difficulty
    Easy = "Ez"
    Moderate = "Md"
    Hard = "Ha"
    Brutal = "Br"
    DIFFICULTY_CHOICE = (
        (Easy, 'Easy'),
        (Moderate, 'Moderate',),
        (Hard, 'Hard'),
        (Brutal, 'Brutal'),
    )
    Difficulty = models.CharField(
        max_length=2,
        choices=DIFFICULTY_CHOICE,
        default=Easy,
    )
    Equipment = models.TextField()
    #Number of People
    Indiv = "Self"
    Pair = "Pair"
    Group = "Group"
    NUM_PPL_CHOICE = (
        (Indiv, "Individual"),
        (Pair, "Pair"),
        (Group, 'Group'),
    )

    NumPeople = models.CharField(
        max_length=4,
        choices=NUM_PPL_CHOICE,
        default=Indiv,

    )

    Time = models.TextField(default='')
    Sets = models.TextField(default='')
    Reps = models.TextField(default='')
    CardStrenFlex = models.TextField(default='')
    Muscles = models.TextField(default='')
    Instructions = models.TextField(default='')
    def __str__(self):
        return self.Name
