from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Like(models.Model):
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    isLike = models.BooleanField()


class Questions_Manager(models.Manager):
    def hot(self):
        return self.order_by('-rating')
    def newest(self):
        return self.order_by('-date_pub')



class Answer(models.Model):

    body = models.TextField(blank=True, db_index=True)
    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    date_pub = models.DateTimeField(auto_now_add=True)
    is_right = models.BooleanField()
    rating = models.IntegerField(null=True)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return self.body
    

class Tag(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, unique=True)
    
    def get_absolute_url(self):
        return reverse('tag_details_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mail = models.EmailField(max_length=50, unique=True)
    nickName = models.CharField(max_length=50, unique=True)
    dateRegistration = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.nickName;

class Question(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    body = models.TextField(db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    

    author = models.ForeignKey('Profile', on_delete=models.CASCADE)
    objects = Questions_Manager()
    tags = models.ManyToManyField('Tag', blank=True, related_name='questions')

    def get_absolute_url(self):
        return reverse('question_details_url', kwargs={'id': self.id})


    def __str__(self):
        return self.title


# Create your models here.
