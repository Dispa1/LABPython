# Generated by Django 4.1.11 on 2023-10-22 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_tag_post_tags'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
