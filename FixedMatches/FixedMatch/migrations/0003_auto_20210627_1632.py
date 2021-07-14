# Generated by Django 3.2.4 on 2021-06-27 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FixedMatch', '0002_auto_20210627_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchDescriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_description',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='prediction_file',
        ),
    ]