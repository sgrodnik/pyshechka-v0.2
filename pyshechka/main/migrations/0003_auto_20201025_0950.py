# Generated by Django 3.1.2 on 2020-10-25 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20201025_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='components',
            new_name='m_components',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='components',
            new_name='p_components',
        ),
    ]