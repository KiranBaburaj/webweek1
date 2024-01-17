
from django.urls import path
from . import views
urlpatterns = [
 
      path('signup/', views.signup),
       path('login/', views.login, name='login'),
           path('logout/', views.logout, name='logout'),
            path('home/', views.home, name='home'),
]
