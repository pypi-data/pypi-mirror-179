# Generated by Django 3.2.14 on 2022-07-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0034_alter_fileattachment_mimetype"),
    ]

    operations = [
        migrations.AddField(
            model_name="scheduledjob",
            name="crontab",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
