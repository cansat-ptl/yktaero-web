# Generated by Django 3.2.8 on 2021-10-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yktaero', '0011_auto_20211019_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='preview_image',
            field=models.FileField(blank=True, help_text='Preview image', upload_to=''),
        ),
    ]
