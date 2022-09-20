# Generated by Django 4.1.1 on 2022-09-20 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0003_investmenthistory"),
    ]

    operations = [
        migrations.CreateModel(
            name="AssetGroup",
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
                ("name", models.CharField(max_length=30, verbose_name="자산그룹명")),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("name", models.CharField(max_length=30, verbose_name="자산그룹명")),
                ("current_price", models.IntegerField(verbose_name="현재가")),
                ("isin", models.CharField(max_length=40, verbose_name="ISIN")),
            ],
        ),
    ]