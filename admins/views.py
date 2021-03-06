from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from products.models import Product, ProductCategory

@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)

class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class UserCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Создание пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Редактирование пользователя'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class ProductsListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Товары'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class CaregoriesListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Админ-панель - Категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


#@user_passes_test(lambda u: u.is_staff)
#def admin_users(request):
#    context = {'title': 'Админ-панель - Пользователи', 'users': User.objects.all()}
#    return render(request, 'admins/admin-users-read.html', context)


#@user_passes_test(lambda u: u.is_staff)
#def admin_users_create(request):
#    if request.method == 'POST':
#        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('admins:admin_users'))
#        else:
#            print(form.errors)
#    else:
#        form = UserAdminRegistrationForm()
#    context = {
#        'title': 'Админ-панель - Создание пользователя', 'form': form}
#    return render(request, 'admins/admin-users-create.html', context)


#@user_passes_test(lambda u: u.is_staff)
#def admin_users_update(request, pk):
#    selected_user = User.objects.get(id=pk)
#    if request.method == 'POST':
#        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('admins:admin_users'))
#        else:
#            print(form.errors)
#    else:
#        form = UserAdminProfileForm(instance=selected_user)
#    context = {
#        'title': 'Админ-панель - Редактирование пользователя',
#        'form': form,
#        'selected_user': selected_user,
#    }
#    return render(request, 'admins/admin-users-update-delete.html', context)


#@user_passes_test(lambda u: u.is_staff)
#def admin_users_remove(request, pk):
#    user = User.objects.get(id=pk)
#    user.is_active = False
#    user.save()
#    return HttpResponseRedirect(reverse('admins:admin_users'))


#Контроллеры для товаров:
#@user_passes_test(lambda u: u.is_staff)
#def admin_products(request):
#    context = {'title': 'Админ-панель - Товары', 'products': Product.objects.all()}
#    return render(request, 'admins/admin-products-read.html', context)

#Контроллеры для категорий:
#@user_passes_test(lambda u: u.is_staff)
#def admin_categories(request):
#    context = {'title': 'Админ-панель - Категории', 'categories': ProductCategory.objects.all()}
#    return render(request, 'admins/admin-categories-read.html', context)