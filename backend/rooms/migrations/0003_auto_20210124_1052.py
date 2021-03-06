# Generated by Django 3.1.4 on 2021-01-24 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('rooms', '0002_room_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='members',
        ),
        migrations.AddField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(related_name='memberset', to='users.User'),
        ),
        migrations.AlterField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownerset', to='users.user'),
        ),
    ]
