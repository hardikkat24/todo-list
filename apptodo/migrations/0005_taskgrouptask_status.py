# Generated by Django 3.0.5 on 2020-04-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptodo', '0004_taskgrouptask'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskgrouptask',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
