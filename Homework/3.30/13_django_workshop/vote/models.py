from django.db import models

# Create your models here.

class Vote(models.Model):
    title = models.CharField(max_length=100)            # 투표 주제
    content1 = models.CharField(max_length=100)          # 한 주제당 항목 2개
    content2 = models.CharField(max_length=100)          # 한 주제당 항목 2개

    def __str__(self):
        return self.title

class Comment(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)        # 한 투표당 댓글 여러개  
    pick = models.BooleanField()
    content = models.CharField(max_length=200)

    def __Str__(self):
        return self.content
    
