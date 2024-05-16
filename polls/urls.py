from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index" ),
    path("<int:question_id>/results", view= views.result),
    path("<int:question_id>", view= views.detail, name= "detail" ),
    path("<int:question_id>/vote", view= views.vote,  name = "vote"),
]