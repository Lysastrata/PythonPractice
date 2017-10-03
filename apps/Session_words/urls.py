from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^words$', views.index),
  url(r'^words/post$', views.color),
  url(r'^words/reset$', views.reset)
]
