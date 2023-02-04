# Generated by Django 4.1.5 on 2023-01-30 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('from', '0004_alter_contact_phone_number_alter_username_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Composer', models.CharField(max_length=200, null=True)),
                ('Title', models.CharField(max_length=200, null=True)),
                ('Artist', models.CharField(max_length=200, null=True)),
                ('Music_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='passport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=200, null=True)),
                ('First_Name', models.CharField(max_length=200, null=True)),
                ('Passport_Number', models.CharField(max_length=200, null=True)),
                ('E_mail', models.EmailField(max_length=200, null=True)),
                ('Passport_Expiry_Date', models.DateTimeField(null=True)),
                ('Passport_Photo', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=200, null=True)),
                ('Flight_Number', models.CharField(max_length=200, null=True)),
                ('Date', models.DateTimeField(null=True)),
                ('Country', models.CharField(max_length=200, null=True)),
                ('Airport', models.CharField(max_length=200)),
            ],
        ),
    ]
