# Generated by Django 4.1.5 on 2023-01-30 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("from", "0003_username_rename_home_player"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="Phone_Number",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="username",
            name="Phone",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
