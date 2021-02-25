# Generated by Django 3.1.6 on 2021-02-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_operatinghours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatinghours',
            name='weekday',
            field=models.CharField(choices=[('Mon', 'Mon'), ('Tue', 'Tue'), ('Wed', 'Wed'), ('Thu', 'Thu'), ('Fri', 'Fri'), ('Sat', 'Sat'), ('Sun', 'Sun')], max_length=3),
        ),
    ]