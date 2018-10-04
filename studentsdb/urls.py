from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from students.views.students import StudentUpdateView, StudentDeleteView

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
    url(r'^groups/(?P<sid>\d+)/edit/$', 'students.views.groups.groups_edit', name='edit_groups'),
    url(r'groups/(?P<sid>\d+)/delete/$', 'students.views.groups.groups_delete', name='delete groups'),

    # Journal
    url(r'^journal/$', 'students.views.journal.journal_list', name='journal'),
    url(r'^journal/(?P<sid>\d+)/$', 'students.views.journal.journal_student', name='student_journal'),
    url(r'^journal/update/$', 'students.views.journal.journal_update', name='update_journal'),

    # Exam
    url(r'^exam/$', 'students.views.exam.exam_list', name="exam"),

    # Contact Admin Form
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin')
)

# Allows you to connect static files
urlpatterns += staticfiles_urlpatterns()
