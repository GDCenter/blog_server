# Generated by Django 2.2.2 on 2019-07-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msg_board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=512, verbose_name='留言内容')),
                ('parent_message', models.IntegerField(max_length=30, verbose_name='回复的留言')),
                ('created_time', models.DateTimeField()),
                ('publisher', models.ForeignKey(on_delete=True, to='user.UserProfile')),
                ('topic', models.ForeignKey(on_delete=True, to='topic.Topic')),
            ],
            options={
                'db_table': 'msg_bolg',
            },
        ),
    ]
