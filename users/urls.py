from django.urls import path
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("<int:feed_id>", views.Modify_User.as_view()),
    path("<str:username>", views.Get_User.as_view()),
]
