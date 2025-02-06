from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("add-task/", views.add_task_view, name="add_task"),
    path("list-tasks/", views.list_tasks_view, name="list_tasks"),
    path("emergency/", views.emergency_alert_view, name="emergency"),
]
 