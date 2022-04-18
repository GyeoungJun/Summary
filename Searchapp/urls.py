from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Searchapp'

urlpatterns = [
    # path('', views.main, name='main'),
    path('category/', views.category, name='category'),
    # path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='signup'),
    
]  