# Generated by Django 3.2.14 on 2022-07-29 21:39

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import nautobot.core.fields
import nautobot.extras.models.mixins
import nautobot.extras.utils
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("extras", "0043_note"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobHook",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("enabled", models.BooleanField(default=True)),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "slug",
                    nautobot.core.fields.AutoSlugField(blank=True, max_length=100, populate_from="name", unique=True),
                ),
                ("type_create", models.BooleanField(default=False)),
                ("type_delete", models.BooleanField(default=False)),
                ("type_update", models.BooleanField(default=False)),
                (
                    "content_types",
                    models.ManyToManyField(
                        limit_choices_to=nautobot.extras.utils.ChangeLoggedModelsQuery,
                        related_name="job_hooks",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        limit_choices_to={"is_job_hook_receiver": True},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_hook",
                        to="extras.job",
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
    ]
