# Generated by Django 4.0.4 on 2022-05-29 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items_app', '0003_remove_item_price_alter_item_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_price', to='items_app.item'),
        ),
    ]
