# Generated by Django 4.1.7 on 2023-04-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_phone_costumer_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='costumer',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pemilikkos',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
