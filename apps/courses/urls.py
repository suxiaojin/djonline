#_*_encoding:utf-8_*_
__date__ = '2017/2/13 22:45'
from django.conf.urls import url,include
from .views import CourseListView,CourseDetailView,CourseInfoView,CommentView
urlpatterns = [
    # 课程相关首页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    url(r'^comment/(?P<course_id>\d+)/$', CommentView.as_view(), name='course_comment'),
]