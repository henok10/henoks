# Generated by Django 4.0.1 on 2022-01-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
