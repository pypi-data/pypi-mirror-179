# Generated by Django 3.2.15 on 2022-08-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0048_alter_objectchange_change_context_detail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(allow_unicode=True, max_length=100, unique=True),
        ),
    ]
