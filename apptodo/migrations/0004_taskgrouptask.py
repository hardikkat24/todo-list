# Generated by Django 3.0.5 on 2020-04-16 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apptodo', '0003_auto_20200412_0222'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskGroupTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=200)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apptodo.TaskGroupList')),
            ],
        ),
    ]
