from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView, ListView

from apps.form import ProductForm
from apps.models import UserModel


# Create your views here.


class UserModelView(ListView):
    template_name = 'index.html'
    queryset = UserModel.objects.all()
    context_object_name = 'users'
class RegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')  # O'zingizning asosiy sahifangizni nomi

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LogoutPageView(LogoutView):
    next_page = reverse_lazy('index')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('index')


def delete_product(request, pk):
    UserModel.objects.filter(id=pk).delete()
    return redirect('index')

class ProductUpdateView(View):
    def get(self, request, product_id):
        product = UserModel.objects.get(id=id)
        form = ProductForm(instance=product)
        return render(request, 'forms.html', {'form': form, 'product': product})

    def post(self, request, product_id):
        product = UserModel.objects.get(id=id)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)  # Güncellenmiş ürün detaylarına yönlendir
        return render(request, 'forms.html', {'form': form, 'product': product})

