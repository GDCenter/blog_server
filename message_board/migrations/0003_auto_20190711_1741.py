# Generated by Django 2.2.2 on 2019-07-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message_board', '0002_auto_20190711_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg_board',
            name='content',
            field=models.CharField(max_length=512, null=True, verbose_name='留言内容'),
        ),
        migrations.AlterField(
            model_name='msg_board',
            name='parent_message',
            field=models.IntegerField(null=True, verbose_name='回复的留言'),
        ),
        migrations.AlterField(
            model_name='msg_board',
            name='publisher',
            field=models.ForeignKey(on_delete=False, to='user.UserProfile'),
        ),
        migrations.AlterField(
            model_name='msg_board',
            name='topic',
            field=models.ForeignKey(on_delete=False, to='topic.Topic'),
        ),
    ]
