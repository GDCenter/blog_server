# Generated by Django 2.2.2 on 2019-07-11 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='msg_board',
            table='message',
        ),
    ]
