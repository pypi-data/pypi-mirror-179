# Generated by Django 3.0.8 on 2020-08-11 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtail_localize", "0006_create_submit_translation_permission"),
    ]

    operations = [
        migrations.AddField(
            model_name="stringtranslation",
            name="tool_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="stringtranslation",
            name="translation_type",
            field=models.CharField(
                choices=[("manual", "Manual"), ("machine", "Machine")],
                default="manual",
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]
