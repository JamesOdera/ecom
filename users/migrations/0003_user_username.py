# Generated by Django 3.0.4 on 2020-03-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
