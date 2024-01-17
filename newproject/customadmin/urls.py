from django.urls import path
from . import views

urlpatterns = [
    path('superuser_login/', views.superuser_login, name='superuser_login'),

    path('custom_admin/', views.custom_admin_homepage, name='custom_admin_homepage'),
  path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),

  path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('user_list/', views.user_list, name='user_list'),
     path('create_user/', views.create_user, name='create_user'),
        path('adlogout/', views.logout_view, name='adlogout'),
        path('search_users/', views.search_users, name='search_users'),


]



