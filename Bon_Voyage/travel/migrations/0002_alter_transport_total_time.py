# Generated by Django 3.2.7 on 2023-03-05 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='total_time',
            field=models.TimeField(),
        ),
    ]
