# Generated by Django 4.1.7 on 2023-04-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_chao_imperium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xeno',
            name='Fac_rule',
            field=models.CharField(max_length=50),
        ),
    ]
