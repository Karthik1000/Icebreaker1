from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status="published")

class post(models.Model):
    objects = models.Manager()
    published = PublishedManager()

    STATUS_CHOICES = {
        ('draft','Draft'),
        ('published','Published'),
    }

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES,default='draft')

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/',null=True, blank=True)
    dob = models.DateTimeField(auto_now_add=True,null=True)
    github_link = models.URLField(max_length=200,null=True)
    facebook_link = models.URLField(max_length=200,null=True)
    linkedIn_link = models.URLField(max_length=200,null=True)
    #email_confirmed = models.BooleanField(default=False)
    # other fields...
    def __str__(self):
        return "Profile {}".format(self.user.username)
