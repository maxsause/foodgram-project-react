# Generated by Django 4.1.7 on 2023-04-04 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cart",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="favorite",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="ingredient",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="ingredientamount",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="recipe",
            options={"ordering": ["-id"]},
        ),
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["-id"]},
        ),
    ]