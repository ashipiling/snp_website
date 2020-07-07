from django.urls import path
 
from . import views
 
urlpatterns = [
           	    path('', views.index, name='index'),
           	    path('sa/', views.detail_sa, name='Staphylococcus'),
           	    path('sm/', views.detail_sm, name='Salmonella'),
           	    path('lm/', views.detail_lm, name='Listeria'),
           	    path('analyse/', views.analyse, name='analyse'),
	            path('upload/', views.upload,name='upload'),
           	    ]
