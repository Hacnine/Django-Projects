# Generated by Django 3.1.4 on 2020-12-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_blog', '0002_post_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Code-Blog', max_length=200),
        ),
    ]
