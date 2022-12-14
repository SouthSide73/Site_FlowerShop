# Generated by Django 4.1 on 2022-09-02 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("siteshop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=50, verbose_name="Адрес")),
                ("email", models.CharField(max_length=30, verbose_name="Email")),
                (
                    "number",
                    models.CharField(max_length=20, verbose_name="Номер телефона"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DirectorItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("vladimir", models.TextField(verbose_name="Слова Владимира")),
                ("abdul", models.TextField(verbose_name="Слова Абдула")),
            ],
        ),
        migrations.CreateModel(
            name="GaleryItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="images", verbose_name="Фото в галерею"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TextItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("job", models.TextField(verbose_name="Наши услуги")),
                ("mission", models.TextField(verbose_name="Почему мы")),
                ("company", models.TextField(verbose_name="О компании")),
            ],
        ),
        migrations.DeleteModel(
            name="SiteItem",
        ),
    ]
