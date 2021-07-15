from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from django.urls import reverse

def index(request):
    context = {'title': 'Админ-панель'}
    return render(request, 'admins/index.html', context)

def admin_users(request):
    context = {'title': 'Админ-панель - Пользователи', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)

def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'Админ-панель - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user,files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
        else:
            print(form.errors)
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Админ-панель - Редактирование пользователя',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

def admin_users_remove(request, pk):
    pass