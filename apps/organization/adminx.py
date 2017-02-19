#_*_encoding:utf-8_*_
__date__ = '2017/1/12 13:46'

import xadmin
from .models import CityDict,CourseOrg,Teacher





xadmin.site.register(CityDict)
xadmin.site.register(CourseOrg)
xadmin.site.register(Teacher)