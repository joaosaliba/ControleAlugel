# Generated by Django 3.1.4 on 2021-04-06 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Aluguel', '0004_auto_20210331_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boleta',
            old_name='imovel',
            new_name='imovel_b',
        ),
        migrations.RenameField(
            model_name='boleta',
            old_name='pessoa',
            new_name='pessoa_b',
        ),
    ]
