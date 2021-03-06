# Generated by Django 3.2.5 on 2021-08-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FixedMatch', '0016_auto_20210821_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='payment_code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.DeleteModel(
            name='PaymentCode',
        ),
    ]
