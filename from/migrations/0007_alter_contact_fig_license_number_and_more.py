# Generated by Django 4.1.5 on 2023-02-01 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('from', '0006_contact_area_code_alter_contact_fig_license_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='FIG_License_Number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Passport_Number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Phone_Number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='State',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Zip_Code',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='Passport_Number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='username',
            name='Passport_Number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='username',
            name='Phone',
            field=models.PositiveIntegerField(),
        ),
    ]
