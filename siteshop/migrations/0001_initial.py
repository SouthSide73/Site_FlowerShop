# Generated by Django 4.1 on 2022-09-02 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteItem",
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
                ("job", models.TextField(verbose_name="Наши услуги")),
                ("mission", models.TextField(verbose_name="Почему мы")),
                ("vladimir", models.TextField(verbose_name="Слова Владимира")),
                ("abdul", models.TextField(verbose_name="Слова Абдула")),
                ("company", models.TextField(verbose_name="О компании")),
                ("email", models.CharField(max_length=30, verbose_name="Email")),
                (
                    "number",
                    models.CharField(max_length=20, verbose_name="Номер телефона"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="images", verbose_name="Галерея"),
                ),
            ],
        ),
    ]
