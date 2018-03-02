from django.urls import path

from . import views

urlpatterns = [
    ##path('', views.homepageview, name = 'home')
   
    path('', views.HomePageView.as_view(), name = 'home'),

    path('about/', views.aboutpageview.as_view(), name = 'about'),

    path('projecta/', views.projectapageview.as_view(), name = 'projecta'),

    path('projectb/', views.projectbpageview.as_view(), name = 'projectb'),

    path('projectc/', views.projectcpageview.as_view(), name = 'projectc'),

]


