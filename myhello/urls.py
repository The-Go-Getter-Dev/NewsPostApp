from django.urls import path
from myhello.views import Myhello
urlpatterns =[
    path('',Myhello.as_view()),
]
