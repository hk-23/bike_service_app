# Generated by Django 3.1.1 on 2020-09-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'owners'), (2, 'customers')], default=0),
        ),
    ]