# Generated by Django 3.1.1 on 2020-09-28 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsapp', '0004_auto_20200928_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='service_on',
        ),
    ]
