# Generated by Django 3.0.6 on 2021-07-15 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Balance', '0002_auto_20210709_0017'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='asset',
            new_name='bonus',
        ),
    ]
