# Generated by Django 3.2.5 on 2021-08-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FixedMatch', '0014_auto_20210821_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcode',
            name='date_added',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymentcode',
            name='payment_code',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
