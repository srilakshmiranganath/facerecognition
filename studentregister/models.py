from django.db import models

class Student(models.Model):
    StudentID = models.CharField(max_length=5, primary_key=True)
    StudentName = models.CharField(max_length=30)
    StudentFace = models.ImageField(blank=False, null=False ,upload_to='media/')

    class Meta:
        db_table = 'student'