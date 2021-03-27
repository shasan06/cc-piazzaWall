from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta, datetime



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
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    expireDateTime = models.DateTimeField(null=True)
    
    #status_list = [('Live', 'Live'), ('Expired', 'Expired')]
    #status = models.CharField(max_length=100, choices=status_list, default='Live')
    status = models.CharField(max_length=30)
    personID = models.ForeignKey(User, on_delete=models.CASCADE)
    likeCount = models.IntegerField(default=0)
    dislikeCount = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)

#the personId is unique and it should be in the post table as a FK(foreign key)
class person(models.Model):
    personID = models.AutoField(primary_key=True)
    personName = models.CharField(max_length=100)


#response table to the post table
#this table(interacton/response) depends on both the above table that is post and owner table
class interaction(models.Model):
    responseID = models.AutoField(primary_key=True)
    postID = models.ForeignKey("post", on_delete=models.CASCADE)
    personID = models.ForeignKey("person", on_delete=models.CASCADE)
    response_list = [('Like', 'Like'), ('Dislike', 'Dislike'),('Comments', 'Comments')]
    response_type = models.CharField(max_length=100, choices=response_list)
    comments = models.CharField(max_length=600)

    #1 logic for expiration time post valid for 7 hours
    @property
    def is_expireDateTime(self):
        expireDateTime = datetime.strftime(self.timestamp + timedelta(hours=7), '%Y-%m-%d  %H:%M:%S' )
        #expireDateTime = datetime.strftime(timezone.now() + timedelta(hours=7), '%Y-%m-%d  %H:%M:%S' )
        return self.expireDateTime

    #2 logic for status 
    @property
    def is_status(self):
        if self.timestamp<self.expireDateTime:#if current time is less than the expiration time then the status is 'Live' otherwise 'Expired'
            status = 'Live'
            return self.status
        else:
            status = 'Expired'
            return self.status
    
    #3 logic for response_type -- like, dislike and comments should become a read only when the time is expired, means the post owner can no longer perform the action
    @property
    def is_response_type1(self):
        if self.timestamp<self.expireDateTime:
            return self.response_type
        else:#when time is expired then response_type should become a diabled and the user can no longer make modification
            response_type = models.CharField(disabled=True)
            return self.response_type

    #4 logic for updating the number of likes, dislikes and comments
    @property
    def is_response_type2(self):
        if self.response_type =='Like':# if the response type is liked by the user then increment the likeCount by one
            self.likeCount +=1
            return self.likeCount
        elif self.response_type =='Dislike': # if the response type is Disliked by the user then increment the DislikeCount by one
            self.dislikeCount +=1
            return self.dislikeCount
        elif self.response_type =='Comment': # if the response type is comment by the user then increment the CommentCount by one
            self.commentCount +=1
            return self.commentCount


            
        '''elif response_type == 'Like' and 'Comment': #if the response type is both comment and like by the user then increment the likecount and commentcount by one
            likeCount +=1 
            commentCount +=1
            return self.likeCount, self.commentCount
        elif response_type == 'DisLike' and 'Comment': #if the response type is both comment and dislike by the user then increment the dislikecount and commentcount by one
            dislikeCount +=1
            commentCount +=1
            return self.dislikeCount, self.commentCount'''
        


    

                  
