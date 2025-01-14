# Generated by Django 5.0.4 on 2024-10-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieWorldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=20)),
                ('year', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
    ]
