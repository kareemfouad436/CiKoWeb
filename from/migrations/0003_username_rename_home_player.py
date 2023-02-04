# Generated by Django 4.1.5 on 2023-01-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("from", "0002_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="username",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Full_Name", models.CharField(max_length=200, null=True)),
                ("User_Name", models.CharField(max_length=200, null=True)),
                ("Email", models.CharField(max_length=200, null=True)),
                ("Phone", models.IntegerField(null=True)),
                ("Passport_Number", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RenameModel(old_name="home", new_name="player",),
    ]
