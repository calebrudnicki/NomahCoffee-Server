# Generated by Django 3.1.6 on 2021-02-23 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0004_auto_20210223_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatinghours',
            name='weekday',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=9),
        ),
    ]
