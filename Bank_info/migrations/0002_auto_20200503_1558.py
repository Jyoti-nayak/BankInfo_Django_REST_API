# Generated by Django 2.2.5 on 2020-05-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_info',
            name='bank_name',
            field=models.CharField(max_length=100),
        ),
    ]
