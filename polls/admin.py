from django.contrib import admin
from .models import Question, Attendence, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Attendence)
admin.site.register(Choice)
