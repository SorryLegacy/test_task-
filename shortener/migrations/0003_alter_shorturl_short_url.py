# Generated by Django 4.0.6 on 2022-08-01 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_shorturl_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='short_url',
            field=models.CharField(max_length=11, unique=True, verbose_name='Short Url'),
        ),
    ]
