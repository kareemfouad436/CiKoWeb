# Generated by Django 4.1.5 on 2023-02-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('from', '0012_alter_contact_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Country',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='FIG_License_Number',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='Name',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='Passport_Number',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='Phone_Number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
