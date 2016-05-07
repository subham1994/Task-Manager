from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^add_todo', 'todo.views.add_todo', name='add_todo'),
    url(r'^delete_todo/(?P<todo_id>\d+)', 'todo.views.delete_todo', name='delete_todo'),
    url(r'^profile/delete_todo/(?P<todo_id>\d+)', 'todo.views.delete_todo_profile', name='delete_todo_profile'),
    url(r'^delete_trash/(?P<todo_id>\d+)', 'todo.views.delete_trash', name='delete_trash'),
    url(r'^edit_todo/(?P<todo_id>\d+)', 'todo.views.edit_todo', name='edit_todo'),
    url(r'^profile/edit_todo/(?P<todo_id>\d+)', 'todo.views.edit_todo_profile', name='edit_todo_profile'),
    url(r'^get_user/(?P<user_id>\d+)', 'todo.views.get_user', name='get_user'),
    url(r'^profile', 'todo.views.profile', name='profile'),
    url(r'^', 'todo.views.home', name='home')
]