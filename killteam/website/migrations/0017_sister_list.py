# Generated by Django 4.1.7 on 2023-04-29 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_remove_kommand_list_unit_kommand_list_unit01_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='sister_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('unit01', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit01', to='website.sister')),
                ('unit02', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit02', to='website.sister')),
                ('unit03', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit03', to='website.sister')),
                ('unit04', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit04', to='website.sister')),
                ('unit05', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit05', to='website.sister')),
                ('unit06', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit06', to='website.sister')),
                ('unit07', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit07', to='website.sister')),
                ('unit08', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit08', to='website.sister')),
                ('unit09', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit09', to='website.sister')),
                ('unit10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='unit10', to='website.sister')),
            ],
        ),
    ]
