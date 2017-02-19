#_*_encoding:utf-8_*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Course,CourseResource
from operation.models import CourseComment
from utils.mixin_utils import LoginRequiredMixin
# Create your views here.

class CourseListView(View):
    def get(self,request):
        all_courses=Course.objects.all().order_by('-add_time')
        hot_courses=Course.objects.all().order_by('-click_nums')[:3]
        #课程搜索
        search_keywords=request.GET.get('keywords', '')
        if search_keywords:
            all_courses=all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))
#课程排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by('-students')
            elif sort == 'hot':
                all_courses = all_courses.order_by('-click_nums')
        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 5, request=request)

        courses = p.page(page)
        return render(request,'course-list.html',{
            'all_courses':courses,
            'sort':sort,
            'hot_courses':hot_courses
        })

class CourseDetailView(View):
    '''
    课程详情
    '''
    def get(self,request,course_id):
        course=Course.objects.get(id=int(course_id))
        '''
        课程点击数加1
       '''
        course.click_nums+=1
        course.save()
        tag=course.tag
        if tag:
            relate_courses=Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses=[]
        return render(request,'course-detail.html',{
            'course':course,
            'relate_courses':relate_courses
        })

class CourseInfoView(LoginRequiredMixin,View):
    '''
    课程章节信息
    '''
    def get(self,request,course_id):
        course_info = Course.objects.get(id=int(course_id))
        course_info.students+=1
        course_info.save()
        all_resources=CourseResource.objects.filter(course=course_info)
        return render(request, 'course-video.html', {
            'course_info': course_info,
            'all_resources':all_resources,

        })

class CommentView(LoginRequiredMixin,View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments=CourseComment.objects.all()
        return render(request, 'course-comment.html', {
            'course': course,
            'all_comments':all_comments,
            'all_resources': all_resources,
        })


