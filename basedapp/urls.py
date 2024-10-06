from django.urls import path
from . import views
from .views import *

urlpatterns = [
     path('', views.index, name='index'),
     path('database_view', views.database_view, name='database'),
     path('<int:pk>/delete', views.deleteinstrument.as_view(), name='delete'),
     path('<int:pk>/update', views.updateinstrument.as_view(), name='update'),
     
 ]
