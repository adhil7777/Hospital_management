from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('home/',views.home,name='home'),
    path('onlinereg/onlinereg',views.onlinereg,name='onlinereg'),    
    path('renewal/renewal',views.renewal,name='renewal'),
    path('renewal2/renewal2',views.renewal2,name='renewal2'),
    path('edit',views.edit),
    path('update',views.update),
    path('delete',views.delete),
    path('emergency/emergency',views.emergency,name='emergency'),
    path('smart/', views.smart_card, name='smart'),
    path('contact/',views.contact,name='contact'),
]
