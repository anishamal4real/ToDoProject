from django.urls import path
from . import views
from .views import TodoCompletedList,TodoList,TodoRetrieveUpdateDestroy, TodoComplete

urlpatterns=[
    path('todos/completed/',views.TodoCompletedList.as_view()),
    path('todos/',views.TodoList.as_view()),
    path('todos/<int:pk>/complete/',views.TodoComplete.as_view()),
    path('todos/<int:pk>/',views.TodoRetrieveUpdateDestroy.as_view()),

]