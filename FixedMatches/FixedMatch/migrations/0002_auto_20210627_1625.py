# Generated by Django 3.2.4 on 2021-06-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FixedMatch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='match_description',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='prediction',
            name='prediction_description',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
