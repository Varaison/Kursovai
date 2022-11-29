from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from .views import *



urlpatterns = [
    path('', ServiceHome.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('register', RegisterUser.as_view(), name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('create', ServiceCreateView.as_view(), name='create'),
    path('service/<slug:service_slug>/', ShowService.as_view(), name='service'),
    path('category/<slug:cat_slug>/', CategoryHome.as_view(), name='category'),
    path('service/<slug:service_slug>/update/', ServiceUpdateView.as_view(), name='update')
]