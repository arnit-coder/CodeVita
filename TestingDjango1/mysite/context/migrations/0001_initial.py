# Generated by Django 3.2.12 on 2022-09-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('Name_Of_your_institution', models.CharField(max_length=40)),
                ('Your_qualifications', models.CharField(max_length=50)),
                ('Linkedin_URL', models.CharField(max_length=50)),
                ('How_did_you_get_to_know_about_us', models.CharField(max_length=30)),
                ('Additional_File', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('Which_track_did_you_want_to_pursue', models.CharField(choices=[('Web development', 'Web development'), ('Data Science', 'Data Science'), ('Computer Vision', 'Computer Vision'), ('Campus Ambassador', 'Campus Ambassador'), ('Blockchain', 'Blockchain'), ('Product Management', 'Product Management'), ('Product Management/Entrepreneur in Residence', 'Product Management/Entrepreneur in Residence'), ('App Development', 'App Development')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BonVoyageApplicationForLiveSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Current_Educational_Qualifications', models.CharField(max_length=100)),
                ('How_did_you_hear_about_us_If_someone_preferred_you_to_us_then_mention_their_name', models.CharField(max_length=30)),
                ('Which_course_did_you_want_to_purchase', models.CharField(choices=[('Python', ''), ('CSS', ''), ('SQL', ''), ('PHP', ''), ('C++', '')], max_length=10)),
                ('When_would_you_like_to_start', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PowershotApplicationForLiveSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Educational_Qualifications', models.CharField(max_length=100)),
                ('Which_course_you_would_like_to_enroll', models.CharField(choices=[('Chrome Extension Using Javascript', 'Chrome Extension Using Javascript'), ('To-do list using React JS', 'To-do list using React JS'), ('Facial Detection Using R', 'Facial Detection Using R'), ('Snake Using Python', 'Snake Using Python'), ('Amazon Clone using React JS', 'Amazon Clone using React JS'), ('Text To Handwriting Using Python', 'Text To Handwriting Using Python'), ('Music Player Using Python', 'Music Player Using Python')], max_length=100)),
                ('Briefly_describe_your_tryst_with_programming', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.CharField(max_length=10)),
                ('College_And_Degree', models.CharField(max_length=100)),
                ('Post_you_would_like_to_apply_for', models.CharField(choices=[('Content Developer', 'Content Developer'), ('SDE', 'Software Development Engineer'), ('BDA', 'Business development associate'), ('Web Developer', 'Web developer')], max_length=50)),
            ],
        ),
    ]
