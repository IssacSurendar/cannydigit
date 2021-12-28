# Generated by Django 3.2.5 on 2021-12-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_contact_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
                ('Banner_Image', models.FileField(upload_to='uploads/%Y/%m/%d')),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('Slug', models.SlugField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='Message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='Proposal',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]