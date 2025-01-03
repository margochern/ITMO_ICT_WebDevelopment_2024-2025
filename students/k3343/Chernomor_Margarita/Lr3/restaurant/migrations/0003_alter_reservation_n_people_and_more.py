# Generated by Django 5.1.3 on 2024-11-30 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_remove_table_restaurant_restaurant_tables"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="n_people",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="time_end",
            field=models.PositiveIntegerField(
                help_text="The start time of the booking",
                validators=[
                    django.core.validators.MaxValueValidator(24),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="time_start",
            field=models.PositiveIntegerField(
                help_text="The start time of the booking",
                validators=[django.core.validators.MaxValueValidator(23)],
            ),
        ),
    ]
