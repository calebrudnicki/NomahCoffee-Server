# Generated by Django 3.1.6 on 2021-07-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0005_remove_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default='', max_length=255, null=True, verbose_name='stripe_id'),
        ),
    ]