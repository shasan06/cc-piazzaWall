from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#this is a post table, the post table will depend on owner table(with ownerID as a Foreign Key)
class post(models.Model):
    postID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    #Topic--politics, health, sports and tech
    politics = models.BooleanField()
    health = models.BooleanField()
    sports = models.BooleanField()
    tech = models.BooleanField()
    message = models.CharField(max_length=240)
    #image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    #expireDateTime = models.DateTimeField(null=True)
    list = [('Live', 'Live'), ('Expired', 'Expired')]
    status = models.CharField(max_length=100, choices=list, default='Live')
    ownerID = models.ForeignKey(User, on_delete=models.CASCADE)

    #the ownerId is the person id and is unique and it should be in the post table as a FK(foreign key)
    class owner(models.Model):
        ownerID = models.AutoField(primary_key=True)
        ownerName = models.CharField(max_length=100)

    #response table to the post table
    #this table(interacton/response) depends on both the above table that is post and owner table
    class interaction(models.Model):
        responseID = models.AutoField(primary_key=True)
        postID = models.ForeignKey("post", on_delete=models.CASCADE)
        ownerID = models.ForeignKey("owner", on_delete=models.CASCADE)
        response_list = [('Like', 'Like'), ('Dislike', 'Dislike'),('Comments', 'Comments')]
        response_type = models.CharField(max_length=100, choices=response_list)
        comments = models.CharField(max_length=600)
                   
