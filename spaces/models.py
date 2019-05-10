from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Space(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('space-detail', kwargs={
            'pk': self.pk
        })
