# Generated by Django 5.1.3 on 2024-11-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0004_remove_restaurant_tables_table_restaurant_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="comment",
            field=models.TextField(blank=True),
        ),
    ]