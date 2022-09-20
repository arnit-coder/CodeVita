from django.db import models


# Create your models here.


class Application(models.Model):
    fields = [
        ('Web development', 'Web development'),
        ('Data Science', 'Data Science'),
        ('Computer Vision', 'Computer Vision'),
        ('Campus Ambassador', 'Campus Ambassador'),
        ('Blockchain', 'Blockchain'),
        ('Product Management', 'Product Management'),
        ('Product Management/Entrepreneur in Residence', 'Product Management/Entrepreneur in Residence'),
        ('App Development', 'App Development')

    ]
    name = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=50, null=True)
    Name_Of_your_institution = models.CharField(max_length=40, null=True)
    Your_qualifications = models.CharField(max_length=50, null=True)
    Linkedin_URL = models.CharField(max_length=50, null=True)
    How_did_you_get_to_know_about_us = models.CharField(max_length=30, null=True)
    #Additional_File = models.FileField(upload_to='documents/%Y/%m/%d/')
    Which_track_did_you_want_to_pursue = models.CharField(choices=fields, max_length=50, null=True)
