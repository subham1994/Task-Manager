from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
	title = models.CharField(max_length=100)
	desc = models.CharField(max_length=1000)
	creator = models.ForeignKey(User, related_name="todos")
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "TODOs"

	def __str__(self):
		return self.title