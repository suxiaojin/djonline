#_*_encoding:utf-8_*_
__date__ = '2017/1/12 13:46'

import xadmin
from .models import UserAsk,CourseComment,UserFavorite,UserMeaasge,UserCourse


xadmin.site.register(UserAsk)
xadmin.site.register(CourseComment)
xadmin.site.register(UserFavorite)
xadmin.site.register(UserMeaasge)
xadmin.site.register(UserCourse)