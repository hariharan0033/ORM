# Generated by Django 4.2.11 on 2024-04-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cgpa',
            field=models.FloatField(),
        ),
    ]
