# Generated by Django 3.1.2 on 2020-10-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
