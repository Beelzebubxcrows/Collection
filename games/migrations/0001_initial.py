# Generated by Django 3.0.3 on 2020-04-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Genre', models.CharField(max_length=20)),
                ('Platform', models.CharField(max_length=20)),
            ],
        ),
    ]