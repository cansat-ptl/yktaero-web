# Generated by Django 3.2.8 on 2021-12-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yktaero', '0017_auto_20211019_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='preview_upload',
            field=models.ImageField(blank=True, help_text='Preview image', upload_to=''),
        ),
    ]
