# Generated by Django 3.1.4 on 2021-02-07 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_search_date_created_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='date_created',
            new_name='from_date',
        ),
        migrations.RenameField(
            model_name='search',
            old_name='date_created_2',
            new_name='to_date',
        ),
    ]
