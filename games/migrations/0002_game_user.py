# Generated by Django 3.0.3 on 2020-04-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
