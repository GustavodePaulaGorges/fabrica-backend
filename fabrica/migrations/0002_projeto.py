# Generated by Django 4.2.4 on 2023-08-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fabrica", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projeto",
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
                ("nome", models.CharField(max_length=200)),
                ("texto", models.CharField(max_length=2500)),
                ("data", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
