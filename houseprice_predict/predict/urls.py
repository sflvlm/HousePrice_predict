from django.conf.urls import url
from predict import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^data_analysis$',views.count)
]