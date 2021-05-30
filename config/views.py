from django.shortcuts import render
from django.views import generic


def base(request):
    return render(request, 'admin/base.html')


def start(request):
    return render(request, 'app/index.html')


def signin(request):
    return render(request, 'admin/login.html')


def signout(request):
    return render(request, 'registration/logged_out.html')


class Signup(generic.TemplateView):
    template_name = 'registration/sign_up.html'


def chart(request):
    return render(request, 'app/chart.html')