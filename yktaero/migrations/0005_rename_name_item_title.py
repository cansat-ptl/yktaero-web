# Generated by Django 3.2.8 on 2021-10-15 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yktaero', '0004_item_preview_docs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='title',
        ),
    ]
