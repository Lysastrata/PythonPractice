from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^randomword$', views.index),
    url(r'^post$', views.post),
    url(r'^randomword/reset$', views.reset)
]
