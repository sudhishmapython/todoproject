from django.urls import path
from todoapp import views

urlpatterns = [

        path('',views.task_add,name='task_add'),
        path('task_view',views.task_view,name='task_view'),
        path('task_delete/<int:dl>',views.task_delete,name='task_delete'),
        path('task_update/<int:up>',views.task_update,name='task_update'),
]
