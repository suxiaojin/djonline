#_*_encoding:utf-8_*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from organization.models import CourseOrg,Teacher

# Create your models here.
class Course(models.Model):
    course_org=models.ForeignKey(CourseOrg,verbose_name=u'课程机构',null=True,blank=True)
    name=models.CharField(max_length=50,verbose_name=u'课程名称')
    desc=models.CharField(max_length=300,verbose_name=u'课程描述')
    teacher = models.ForeignKey(Teacher,verbose_name=u'讲师',null=True,blank=True)
    detail=models.TextField(verbose_name=u'课程详情')
    degree=models.CharField(choices=(('cj','初级'),('zj','中级'),('gj','高级')),max_length=2)
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums=models.IntegerField(default=0, verbose_name=u'收藏人数')
    is_banner=models.BooleanField(verbose_name=u'是否轮播',default=False)
    image=models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
    click_nums=models.IntegerField(default=0,verbose_name=u'点击数')
    category = models.CharField(max_length=20, verbose_name=u'课程类别',default='')
    tag = models.CharField(max_length=20, verbose_name=u'课程标签',default='')
    add_time=models.DateField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'课程'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name
    def get_zj_num(self):
        '''
        获取课程章节数

        '''
        return self.lesson_set.all().count()

    def get_learn_user(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        '''
        获取课程章节

        '''
        return self.lesson_set.all()


class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name=u'课程')
    name=models.CharField(max_length=100,verbose_name=u'章节名')
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')

    class Meta:
        verbose_name=u'章节'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        '''
        获取章节视频

        '''
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(max_length=100, verbose_name=u"视频名")
    url = models.CharField(max_length=100, verbose_name=u"访问地址",default='')
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name=u'视频'
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
        course=models.ForeignKey(Course,verbose_name=u'课程')
        name = models.CharField(max_length=100, verbose_name=u"资源名称")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
        download=models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件",max_length=100)

        class Meta:
            verbose_name = u'课程资源'
            verbose_name_plural = verbose_name

        def __unicode__(self):
            return self.name
