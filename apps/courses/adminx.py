#_*_encoding:utf-8_*_
import xadmin
from .models import Course,Lesson,Video,CourseResource




xadmin.site.register(Course)
xadmin.site.register(Lesson)
xadmin.site.register(Video)
xadmin.site.register(CourseResource)