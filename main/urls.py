from django.urls import path
from main import views


urlpatterns = [
    path('', views.homepage, name = 'homepage' ),
    path('home/', views.homepage, name = 'homepage' ),
    path('about/', views.aboutpage, name = 'aboutpage' ),
    path('contact/', views.contactpage, name = 'contactpage' ),
]