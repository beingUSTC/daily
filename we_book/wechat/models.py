from django.db import models

# Create your models here.
#django默认会为每个model类添加如下语句：id = models.AutoField(primary_key=True)
# 当其他字段添加了primary_key属性，则不会创建id字段了


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    type = models.BooleanField()#true代表老师，false代表学生
    Class = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    brief = models.TextField()
    location = models.CharField(max_length=32)


class bookcollect(models.Model):
   userid = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
   bookid = models.ForeignKey(Book,on_delete=models.CASCADE)


class Task(models.Model):
    Class = models.IntegerField()
    title = models.CharField(max_length=100)
    dateline = models.DateField(verbose_name='截止日期')

