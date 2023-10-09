from django.urls import path
from member import views

urlpatterns = [
    path('',views.index),
    path('coffee',views.coffee),
    path('maker',views.maker)
]