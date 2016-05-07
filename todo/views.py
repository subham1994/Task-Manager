from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from todo.models import ToDo
from todo.forms import ToDoForm
from django.contrib.auth.models import User

def delete_db_entry(id):
	try:
		todo_to_delete = ToDo.objects.filter(pk=id)
		todo_to_delete.update(is_deleted=True)
	except ToDo.DoesNotExist:
		# todo doesn't exist with the given id, do nothing.
		pass

def get_profile_data(todos):
	pending_todos = todos.exclude(is_deleted=True).order_by('-created_at')
	deleted_todos = todos.filter(is_deleted=True).order_by('-updated_at')
	return (pending_todos, deleted_todos)

def home(request):
	todos = ToDo.objects.all().order_by('-created_at').exclude(is_deleted=True)
	return render_to_response('todos.html', {'todos': todos}, context_instance=RequestContext(request))

def delete_todo(request, todo_id):
	delete_db_entry(todo_id)
	return HttpResponseRedirect('/')

def delete_todo_profile(request, todo_id):
	delete_db_entry(todo_id)
	return HttpResponseRedirect('/profile')

@login_required
def add_todo(request):
	if request.method == "POST":
		form = ToDoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.creator = request.user
			todo.save()
			return HttpResponseRedirect('/')
	else:
		form = ToDoForm()
	return render_to_response('add_todo.html', {'form': form}, context_instance=RequestContext(request))

def edit_todo_helper(request_obj, todo_id, redirect_to=''):
	todo = ToDo.objects.filter(pk=todo_id)
	if request_obj.method == "POST":
		form = ToDoForm(request_obj.POST)
		if form.is_valid():
			title = request_obj.POST['title']
			desc = request_obj.POST['desc']
			todo.update(title=title, desc=desc)
			return HttpResponseRedirect('/' + redirect_to)
	else:
		form = ToDoForm(initial={'title': todo[0].title, 'desc': todo[0].desc})
	return render_to_response('add_todo.html', {'form': form, 'action': 'edit_todo/' + str(todo_id)}, 
							   context_instance=RequestContext(request_obj))


def edit_todo(request, todo_id):
	return edit_todo_helper(request, todo_id)

def edit_todo_profile(request, todo_id):
	return edit_todo_helper(request, todo_id, 'profile')

@login_required
def profile(request):
	todos = ToDo.objects.filter(creator=request.user)
	pending_todos, deleted_todos = get_profile_data(todos)
	return render_to_response('profile.html', {'todos': pending_todos, 'deleted_todos': deleted_todos}, 
							   context_instance=RequestContext(request))

def delete_trash(request, todo_id):
	try:
		todo_to_delete = ToDo.objects.get(pk=todo_id)
		todo_to_delete.delete()
	except ToDo.DoesNotExist:
		# todo doesn't exist with the given id, do nothing.
		pass
	return HttpResponseRedirect('/profile')

def get_user(request, user_id):
	try:
		user = User.objects.get(pk=user_id)
		todos = ToDo.objects.filter(creator=user_id)
		pending_todos, deleted_todos = get_profile_data(todos)
		if user == request.user:
			return HttpResponseRedirect('/profile')
	except User.DoesNotExist:
		pass
	return render_to_response('profile.html', {'todos': pending_todos, 'deleted_todos': deleted_todos, 'diff_user': True, 'cur_user': user}, 
							  context_instance=RequestContext(request))