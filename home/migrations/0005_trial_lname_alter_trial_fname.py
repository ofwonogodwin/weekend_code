# Generated by Django 5.1.7 on 2025-03-29 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_trial_fname'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='lname',
            field=models.CharField(default='Last Name', max_length=50),
        ),
        migrations.AlterField(
            model_name='trial',
            name='fname',
            field=models.CharField(default='First Name', max_length=50),
        ),
    ]
