from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse



class Category(models.Model):
    HOLLYWOOD      = 'HollyWood'
    BOLLYWOOD      = 'BollyWood'
    INDIAN_BANGLA  = 'Indian_Bangla'
    TAMIL          = 'Tamil'
    INDIAN_OTHERS  = 'Indian_ohers'
    BANGLADESH     = 'Bangladesh'
    FOREIGN        = 'Foreign'
    CATEGORY_NAME_CHOICE = (
        (HOLLYWOOD, 'Hollywood'),
        (BOLLYWOOD, 'Bollywood'),
        (INDIAN_BANGLA, 'Indian_bangla'),
        (TAMIL, 'TamiL'),
        (INDIAN_OTHERS, 'Indian_other'),
        (BANGLADESH, 'BangLadesh'),
        (FOREIGN, 'Foreign'),
    )
    name    = models.CharField(max_length=120, choices=CATEGORY_NAME_CHOICE, default=HOLLYWOOD,)


    class Meta:
        ordering = ('name',)

    def __str__(self):
        return "{}" .format(self.name)

    def get_absolate_url(self):
        return reverse('category', args[self.name])




class Genera(models.Model):
    ACTION     = 'Action'
    SCI_FI     = 'Sci-Fi'
    DRAMA      = 'Drama'
    THRILLER   = 'Thriller'
    ADVENTURE  = 'Adventure'
    ROMANTIC   = 'Romantic'
    HOROR      = 'Horor'
    GENERA_NAME_CHOICE = (
        (ACTION, 'Action'),
        (SCI_FI, 'Sci-Fi'),
        (DRAMA, 'Drama'),
        (ADVENTURE, 'Adventure'),
        (ROMANTIC, 'Romantic'),
        (HOROR, 'Horor'),
        (THRILLER, 'Thriller'),
    )
    name    = models.CharField(max_length=120, choices=GENERA_NAME_CHOICE, default=ACTION,)

    def __str__(self):
        return "{}" .format(self.name)


class Director(models.Model):
    name      = models.CharField(max_length=150)
    born      = models.DateField()
    died      = models.DateField(null = True, blank = True )
    biography = models.TextField(null = True)
    image     = models.ImageField(default='default.png', blank = True)


    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name      = models.CharField(max_length=150)
    born      = models.DateField()
    died      = models.DateField(null = True, blank = True )
    biogrphy  = models.TextField()
    image     = models.ImageField(default='default.png', blank = True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

class Writter(models.Model):
    name      = models.CharField(max_length=150)
    born      = models.DateField()
    died      = models.DateField(null = True, blank = True )
    biogrphy  = models.TextField()
    image     = models.ImageField(default='default.png', blank = True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title       = models.CharField(max_length=120)
    plot        = models.TextField(max_length=400, blank=True)
    writers     = models.ForeignKey(Writter, on_delete=models.CASCADE)
    director    = models.ForeignKey(Director, on_delete=models.CASCADE)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    genera      = models.ManyToManyField(Genera, related_name='genera')
    length      = models.IntegerField()
    ratings     = models.PositiveIntegerField(default = 0)
    year        = models.PositiveIntegerField(default = 0)
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True)
    actors      = models.ManyToManyField(Actor, related_name='actors')
    review1     = models.TextField(blank=True)
    review2     = models.TextField(blank=True)
    review3     = models.TextField(blank=True)
    view        = models.PositiveIntegerField(default = 0,blank=True)
    time        = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    image       = models.ImageField(default='default.png', blank = True)
    image2      = models.ImageField(default='default.png', blank = True)
    image3      = models.ImageField(default='default.png', blank = True)


    class Meta:
        ordering = ('-time',)

    def __str__(self):
        return " {} ({}) " .format(self.title, self.year)



"""Commnet Section Model"""
class Comment(models.Model):
    content    = models.TextField()
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank = True)
    post       = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
