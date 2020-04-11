# Generated by Django 3.0.3 on 2020-04-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Year', models.IntegerField(blank=True)),
                ('Genre', models.CharField(max_length=10)),
            ],
        ),
    ]