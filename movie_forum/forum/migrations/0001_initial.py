# Generated by Django 3.2.7 on 2022-06-23 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('movie', models.CharField(max_length=100)),
            ],
        ),
    ]
