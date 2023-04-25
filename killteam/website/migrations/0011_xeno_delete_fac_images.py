# Generated by Django 4.1.7 on 2023-04-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_fac_images_remove_kommando_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xeno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fac_name', models.CharField(max_length=50)),
                ('Fac_rule', models.CharField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Fac_images',
        ),
    ]
