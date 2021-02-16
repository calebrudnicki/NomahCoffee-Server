# Generated by Django 3.1.6 on 2021-02-12 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiapp.coffee')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]