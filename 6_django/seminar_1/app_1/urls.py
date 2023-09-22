from django.urls import include, path
from . import views

urlpatterns = [
    path('app1/', views.index, name='index'),
]
