from django.urls import path
from admins.views import index, UserListView, UserCreateView, UserUpdateView, \
    UserDeleteView, admin_products, admin_categories

app_name = 'admins'
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users/create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='admin_users_update'),
    path('users/remove/<int:pk>/', UserDeleteView.as_view(), name='admin_users_remove'),
    path('products/', admin_products, name='admin_products'),
    path('categories/', admin_categories, name='admin_categories'),

]