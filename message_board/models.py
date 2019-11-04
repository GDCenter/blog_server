from django.db import models
from topic.models import Topic
from user.models import UserProfile
# Create your models here.

class Msg_board(models.Model):
    content = models.CharField(verbose_name='留言内容',max_length=512,null=True)
    parent_message = models.IntegerField(verbose_name='回复的留言',null=True)
    topic = models.ForeignKey(Topic,on_delete=False)
    publisher = models.ForeignKey(UserProfile,on_delete=False)
    created_time = models.DateTimeField()

    class Meta:
        db_table='message'