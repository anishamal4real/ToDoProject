from django.urls import path
from . import views

urlpatterns=[
    path('todoscompleted/',views.TodoCompletedList.as_view()),
]