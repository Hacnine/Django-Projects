# Generated by Django 3.1.4 on 2021-02-07 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='date_created_2',
            field=models.DateTimeField(null=True),
        ),
    ]
