from django.urls import path

from . import views

urlpatterns = [path('', views.index, name='index'),
               path('<int:pk>/', views.details, name='id'),
               path('<int:pk>/results/',
                    views.results, name='results'),
               path('<int:user_id>/name/', views.names, name='vote'),
               path('specifics/<int:user_id>/', views.details, name='details'), ]
