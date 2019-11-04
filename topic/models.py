from django.db import models
from user.models import UserProfile



#迁移指定模块

# Python3 manange.py makemigrations topic
#Python3 manange.py migrate topic

#mysql 查询指定的创建语句 show create table topic

# Create your models here.
class Topic(models.Model):

    """
    主键为id,django默认添加
    """
    # id = models.IntegerField(primary_key=True,auto_created=True)
    #文章标题
    title = models.CharField(verbose_name='题目',null=False ,max_length=50)
    #作者
    author = models.ForeignKey(UserProfile,on_delete=False,verbose_name='作者')
    # tec 技术类的  & 非技术类的
    category = models.CharField(max_length=20,verbose_name='分类')
    #limit - public 公开的,所有人可见, & private 私有的,博主可看
    limit = models.CharField(max_length=10,verbose_name='文章权限')
    introduce = models.CharField(max_length=90,verbose_name='文章简介')
    content = models.TextField(verbose_name='正文')
    #文章创建时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()




    class Meta:
        db_table='topic'