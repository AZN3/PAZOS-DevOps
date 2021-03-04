from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('random/', views.randomString, name='randomString'),
    path('hasher/', views.hasher, name='hasher'),
    path('hasher/your_hash', views.your_hash, name='your_hash'),
    path('details/',views.details,name='details'),
    path('ip_checker/',views.ip_address,name='ip_checker'),
    path('ip_checker/your_IP',views.your_IP,name='your_IP'),
]