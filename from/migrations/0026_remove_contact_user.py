# Generated by Django 4.1.5 on 2023-02-04 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('from', '0025_alter_contact_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
