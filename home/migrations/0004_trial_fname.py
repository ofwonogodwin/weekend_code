# Generated by Django 5.1.7 on 2025-03-29 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_trial_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='fname',
            field=models.CharField(default='Last Name', max_length=50),
        ),
    ]
