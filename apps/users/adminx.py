#_*_encoding:utf-8_*_
__date__ = '2017/1/12 13:46'

import xadmin
from xadmin import views
from .models import UserProfile,EmailVerifyRecord,Banner


class BaseSetting(object):
    enable_themes= True
    use_bootswatch=True

class GlobalSettings(object):
    site_title="djonline后台管理系统"
    site_footer='Djonline'
    menu_style='accordion'


class EmailVerifyRecordAdmin(object):
    list_display=['code','email']
    search_fields=['code','email']
    list_filter=['code','email']

xadmin.site.register(UserProfile)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)
