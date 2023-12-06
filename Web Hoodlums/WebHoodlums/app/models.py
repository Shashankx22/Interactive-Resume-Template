# import os
# from django.conf import settings
from django.db import models

# Create your models here.

# models.py
# from django.db import models

class ResumeData(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    locationvalue = models.CharField(max_length=100)
    description = models.TextField()
    language1 = models.CharField(max_length=255, default='Default language')
    language2 = models.CharField(max_length=255, default='Default language')
    language3 = models.CharField(max_length=255, default='Default language')
    language4 = models.CharField(max_length=255, default='Default language')
    Professional_Skill_1 = models.CharField(max_length=255, default='Default Skill')
    skill_range1 = models.IntegerField(default=0)
    Professional_Skill_2 = models.CharField(max_length=255, default='Default Skill')
    skill_range2 = models.IntegerField(default=0)
    Professional_Skill_3 = models.CharField(max_length=255, default='Default Skill')
    skill_range3 = models.IntegerField(default=0)
    Professional_Skill_4 = models.CharField(max_length=255, default='Default Skill')
    skill_range4 = models.IntegerField(default=0)
    Technical_Skill_1 = models.CharField(max_length=255, default='Default Skill')
    skill_range5 = models.IntegerField(default=0)
    Technical_Skill_2 = models.CharField(max_length=255, default='Default Skill')
    skill_range6 = models.IntegerField(default=0)
    Technical_Skill_3 = models.CharField(max_length=255, default='Default Skill')
    skill_range7 = models.IntegerField(default=0)
    Technical_Skill_4 = models.CharField(max_length=255, default='Default Skill')
    skill_range8 = models.IntegerField(default=0)
    eduname1 = models.CharField(max_length=255, default='Default Name')
    Uni1 = models.CharField(max_length=255, default='Default Name')
    startdate = models.IntegerField(default=2000)
    enddate = models.IntegerField(default=2000)
    edudes = models.TextField(max_length=255, default='Default Description')
    eduname2 = models.CharField(max_length=255, default='Default Name')
    Uni2 = models.CharField(max_length=255, default='Default Name')
    startdate2 = models.IntegerField(default=2000)
    enddate2 = models.IntegerField(default=2000)
    edudes2 = models.TextField(max_length=255, default='Default Description')
    eduname3 = models.CharField(max_length=255, default='Default Name')
    Uni3 = models.CharField(max_length=255, default='Default Name')
    startdate3 = models.IntegerField(default=2000)
    enddate3 = models.IntegerField(default=2000)
    edudes3 = models.TextField(max_length=255, default='Default Description')
    Domain1 = models.CharField(max_length=255, default='Default Domain')
    Description1 = models.TextField(default='Default Description')
    Domain2 = models.CharField(max_length=255, default='Default Domain')
    Description2 = models.TextField(default='Default Description')
    Domain3 = models.CharField(max_length=255, default='Default Domain')
    Description3 = models.TextField(default='Default Description')
    Project_Name1 = models.CharField(max_length=255, default='Default Project')
    Project_Domain1 = models.CharField(max_length=255, default='Default Domain')
    Project_Description1 = models.TextField(max_length=255, default='Default Description')
    url1 = models.URLField(default='url')
    Project_Name2 = models.CharField(max_length=255, default='Default Project')
    Project_Domain2 = models.CharField(max_length=255, default='Default Domain')
    Project_Description2 = models.TextField(max_length=255, default='Default Description')
    url2 = models.URLField(default='url')
    Project_Name3 = models.CharField(max_length=255, default='Default Project')
    Project_Domain3 = models.CharField(max_length=255, default='Default Domain')
    Project_Description3 = models.TextField(max_length=255, default='Default Description')
    url3 = models.URLField(default='url')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name