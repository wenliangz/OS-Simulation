# Generated by Django 2.0.3 on 2018-03-26 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memschedalg',
            name='demourl',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
