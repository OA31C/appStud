from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'studentsdb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Students List
    url(r'^$', 'students.views.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students_add', name='add'),
    url(r'^students/[0-9]+/edit/$', 'students.views.students_edit', name='edit_students'),
    url(r'^students/[0-9]+/delete/$', 'students.views.students_delete', name='delete_students'),

    # Groups
    url(r'^groups/$', 'students.views.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups_add', name='add_groups'),
    url(r'^groups/[0-9]+/edit/$', 'students.views.groups_edit', name='edit_groups'),
    url(r'groups/[0-9]+/delete/$', 'students.views.groups_delete', name='delete groups'),

    # Journal
    url(r'^journal/$', 'students.views.journal_list', name='journal'),
    url(r'^journal/[0-9]+/$', 'students.views.journal_student', name='student_journal'),
    url(r'^journal/update/$', 'students.views.journal_update', name='update_journal'),
)
