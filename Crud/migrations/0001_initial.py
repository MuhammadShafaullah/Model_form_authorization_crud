# Generated by Django 4.1 on 2022-10-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('password', models.CharField(max_length=70)),
                ('rpassword', models.CharField(max_length=70)),
            ],
        ),
    ]
