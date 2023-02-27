from django.urls import path
from . import views

urlpatterns = [
    path("", views.Reviews.as_view()),
    path("<int:review_id>", views.Modify_Review.as_view()),
]
