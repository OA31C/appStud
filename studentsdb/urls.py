from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Students List
    url(r'^$', 'students.views.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students_edit', name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students_delete', name='students_delete'),

    # Groups
    url(r'^groups/$', 'students.views.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups_add', name='add_groups'),
    url(r'^groups/(?P<sid>\d+)/edit/$', 'students.views.groups_edit', name='edit_groups'),
    url(r'groups/(?P<sid>\d+)/delete/$', 'students.views.groups_delete', name='delete groups'),

    # Journal
    url(r'^journal/$', 'students.views.journal_list', name='journal'),
    url(r'^journal/(?P<sid>\d+)/$', 'students.views.journal_student', name='student_journal'),
    url(r'^journal/update/$', 'students.views.journal_update', name='update_journal'),
)
