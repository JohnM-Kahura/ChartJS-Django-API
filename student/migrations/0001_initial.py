# Generated by Django 4.1 on 2022-08-07 15:02

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
                ('name', models.CharField(max_length=50)),
                ('maths', models.CharField(max_length=50)),
                ('english', models.CharField(max_length=50)),
                ('biology', models.CharField(max_length=50)),
                ('chemistry', models.CharField(max_length=50)),
                ('history', models.CharField(max_length=50)),
                ('physics', models.CharField(max_length=50)),
            ],
        ),
    ]