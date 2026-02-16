from django.urls import path
from .views import task_list, delete_task

urlpatterns = [
    path('', task_list),
    path('delete/<int:task_id>/', delete_task),
]

