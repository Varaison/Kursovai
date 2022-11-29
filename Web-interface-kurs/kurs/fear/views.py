from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import *
from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from django.http import *
from .forms import *
from django.contrib.auth.mixins import *


class ServiceCreateView(LoginRequiredMixin, CreateView):
    template_name = 'fear/create.html'
    form_class = ServiceForm
    extra_context = {'title': 'Добавление'}
    login_url = '/admin/'


class ServiceUpdateView(UpdateView):
    template_name = 'fear/update.html'
    form_class = ServiceForm
    model = Service
    slug_url_kwarg = 'service_slug'
    success_url = reverse_lazy('home')


class ServiceHome(ListView):
    template_name = 'fear/index.html'
    context_object_name = 'service'
    extra_context = {'title': 'МузПросвет'}
    model = Service
    paginate_by = 6

    def get_queryset(self):
        return Service.objects.all().select_related('cat')


class ShowService(DetailView):
    model = Service
    template_name = 'fear/service.html'
    slug_url_kwarg = 'service_slug'


class CategoryHome(ListView):
    template_name = 'fear/index.html'
    paginate_by = 3
    context_object_name = 'service'
    extra_context = {'title': 'МузПросвет'}
    model = Service

    def get_queryset(self):
        return Service.objects.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')


def about(request):
    if request.GET:
        print(request.GET)
    context = {'title': 'Контакты'}
    return render(request, 'fear/about.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не существует</h1>')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'fear/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'fear/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')
