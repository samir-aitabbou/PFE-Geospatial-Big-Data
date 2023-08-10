# spark_app/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path('members/', views.members, name='members'),

    path('test_spark_connection/', views.test_spark_connection, name='test_spark_connection'),
    path('read_netcdf/', views.read_netcdf_from_hdfs, name='read_netcdf'),
]
