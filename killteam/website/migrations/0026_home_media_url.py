# Generated by Django 4.1.7 on 2023-04-29 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_home_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_media',
            name='url',
            field=models.CharField(blank=True, max_length=50000, null=True),
        ),
    ]
