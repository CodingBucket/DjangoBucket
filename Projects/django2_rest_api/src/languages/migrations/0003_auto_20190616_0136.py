# Generated by Django 2.2.2 on 2019-06-15 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20190616_0134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmer',
            old_name='languges',
            new_name='languages',
        ),
    ]
