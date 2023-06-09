# Generated by Django 4.1.7 on 2023-04-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0028_alter_transaction_barang_dibeli'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='buktiTransfer',
            field=models.ImageField(blank=True, null=True, upload_to='bukti/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='rentalFrequency',
            field=models.CharField(blank=True, choices=[('Year', 'Year'), ('Month', 'Month'), ('Week', 'Week'), ('Day', 'Day')], max_length=20, null=True),
        ),
    ]
