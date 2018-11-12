from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from students.views.students import StudentUpdateView, StudentDeleteView
from students.views.journal import JournalView
from students.views.groups import GroupUpdateView, GroupDeleteView
from students.views.exam import ExamUpdateView, ExamDeleteView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Students List
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add', name='add_groups'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='edit_groups'),
    url(r'groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='delete groups'),

    # Journal
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
    # Exam
    url(r'^exam/$', 'students.views.exam.exam_list', name="exam"),
    url(r'^exam/add/$', 'students.views.exam.exam_add', name='exam_add'),
    url(r'^exam/(?P<pk>\d+)/edit/$', ExamUpdateView.as_view(), name='edit_exam'),
    url(r'^exam/(?P<pk>\d+)/delete/$', ExamDeleteView.as_view(), name='delete_exam'),

    # Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin')
)

# Allows you to connect static files
urlpatterns += staticfiles_urlpatterns()
