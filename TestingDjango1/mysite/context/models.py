from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=40)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=10)
    College_And_Degree = models.CharField(max_length=100)
    Post_choices = (
        ('Content Developer', 'Content Developer'),
        ('SDE', 'Software Development Engineer'),
        ('BDA', 'Business development associate'),
        ('Web Developer', 'Web developer')
    )
    Post_you_would_like_to_apply_for = models.CharField(max_length=50, choices=Post_choices)


class PowershotApplicationForLiveSeries(models.Model):
    name = models.CharField(max_length=40)
    Email = models.EmailField()
    Educational_Qualifications = models.CharField(max_length=100)
    Course_choice = (
        ('Chrome Extension Using Javascript', 'Chrome Extension Using Javascript'),
        ('To-do list using React JS', 'To-do list using React JS'),
        ('Facial Detection Using R', 'Facial Detection Using R'),
        ('Snake Using Python', 'Snake Using Python'),
        ('Amazon Clone using React JS', 'Amazon Clone using React JS'),
        ('Text To Handwriting Using Python', 'Text To Handwriting Using Python'),
        ('Music Player Using Python', 'Music Player Using Python')
    )
    Which_course_you_would_like_to_enroll = models.CharField(choices=Course_choice, max_length=100)
    Briefly_describe_your_tryst_with_programming = models.TextField(max_length=100)


class How_did_you_hear_about_us_If_someone_preferred_you_to_us_then_mention_their_name:
    pass


class BonVoyageApplicationForLiveSeries(models.Model):
    name = models.CharField(max_length=40)
    Email = models.EmailField()
    Current_Educational_Qualifications = models.CharField(max_length=100)
    How_did_you_hear_about_us_If_someone_preferred_you_to_us_then_mention_their_name = models.CharField(max_length=30)
    Course_list = (
        ('Python', ''),
        ('CSS', ''),
        ('SQL', ''),
        ('PHP', ''),
        ('C++', '')
    )
    Which_course_did_you_want_to_purchase = models.CharField(max_length=10, choices=Course_list)
    When_would_you_like_to_start = models.DateTimeField()


class Application(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    Name_Of_your_institution = models.CharField(max_length=40)
    Your_qualifications = models.CharField(max_length=50)
    Linkedin_URL = models.CharField(max_length=50)
    How_did_you_get_to_know_about_us = models.CharField(max_length=30)
    Additional_File = models.FileField(upload_to='documents/%Y/%m/%d/')
    fields = (
        ('Web development', 'Web development'),
        ('Data Science', 'Data Science'),
        ('Computer Vision', 'Computer Vision'),
        ('Campus Ambassador', 'Campus Ambassador'),
        ('Blockchain', 'Blockchain'),
        ('Product Management', 'Product Management'),
        ('Product Management/Entrepreneur in Residence', 'Product Management/Entrepreneur in Residence'),
        ('App Development', 'App Development')

    )
    Which_track_did_you_want_to_pursue = models.CharField(choices=fields, max_length=50)
