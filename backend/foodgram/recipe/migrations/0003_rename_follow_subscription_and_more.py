# Generated by Django 4.1.7 on 2023-04-03 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("recipe", "0002_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Follow",
            new_name="Subscription",
        ),
        migrations.RemoveConstraint(
            model_name="subscription",
            name="unique_follow",
        ),
        migrations.RenameField(
            model_name="subscription",
            old_name="author",
            new_name="following",
        ),
        migrations.AlterField(
            model_name="favorite",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="is_favorited",
                to="recipe.recipe",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AlterField(
            model_name="shoppingcart",
            name="recipe",
            field=models.ManyToManyField(
                related_name="is_in_shopping_cart",
                to="recipe.recipe",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AddConstraint(
            model_name="subscription",
            constraint=models.UniqueConstraint(
                fields=("user", "following"), name="unique_follow"
            ),
        ),
    ]