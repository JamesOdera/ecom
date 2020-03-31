# Generated by Django 3.0.4 on 2020-03-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('userType', models.CharField(max_length=60)),
                ('status', models.CharField(max_length=60)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
