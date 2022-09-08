from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    bio = models.TextField(max_length=400, blank=True, null=True)
    profile_img = models.ImageField(upload_to='profile_images', default='kyle.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    body = models.TextField()
    tag = models.ForeignKey(Tag, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    post_img = models.ImageField(upload_to='post_images', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "Comment by {}".format(self.user.username)




    