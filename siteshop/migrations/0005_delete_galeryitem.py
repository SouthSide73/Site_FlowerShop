# Generated by Django 4.1 on 2022-09-03 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("siteshop", "0004_delete_contactitem_delete_directoritem"),
    ]

    operations = [
        migrations.DeleteModel(
            name="GaleryItem",
        ),
    ]
