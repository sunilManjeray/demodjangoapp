from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
               path('<int:user_id>/', views.details, name='id'),
               path('<int:user_id>/results/',
                    views.results, name='results'),
               path('<int:user_id>/name/', views.names, name='vote'),
               path('specifics/<int:user_id>/', views.details, name='details'), ]
