# Generated by Django 2.2.17 on 2020-12-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address1", models.CharField(max_length=256)),
                ("address2", models.CharField(max_length=256)),
                ("city", models.CharField(max_length=256)),
                ("state", models.CharField(max_length=256)),
                ("zip", models.CharField(max_length=256)),
            ],
        ),
    ]
