# Generated by Django 3.2.5 on 2021-12-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_contacts_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
