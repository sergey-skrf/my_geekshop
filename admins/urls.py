from django.urls import path
from admins.views import index, admin_users, admin_users_create, admin_users_update, \
    admin_users_remove, admin_products, admin_categories

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users/create/', admin_users_create, name='admin_users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='admin_users_update'),
    path('users/remove/<int:pk>/', admin_users_remove, name='admin_users_remove'),
    path('products/', admin_products, name='admin_products'),
    path('categories/', admin_categories, name='admin_categories'),

]