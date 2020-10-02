# Generated by Django 3.1.1 on 2020-09-30 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsapp', '0006_auto_20200929_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('canceled', 'Canceled'), ('ready', 'Ready'), ('delivered', 'Delivered')], default='pending', max_length=15),
        ),
    ]
