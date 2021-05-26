from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from authapp.models import User
from adminapp.forms import UserAdminRegistrerForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/admin.html')


# @user_passes_test(lambda u: u.is_superuser)
# def admin_user_read(request):
#     context = {'users': User.objects.all()}
#     return render(request, 'adminapp/admin-users-read.html', context)


class UserListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'


class UserCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    form_class = UserAdminRegistrerForm
    success_url = reverse_lazy('admin_staff:admin_users_read')


class UserUpdateView(UpdateView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')
    form_class = UserAdminProfileForm


class UserDeleteView(DeleteView):
    model = User
    template_name = 'adminapp/admin-users-update-delete.html'
    success_url = reverse_lazy('admin_staff:admin_users_read')

