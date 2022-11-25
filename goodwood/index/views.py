import random

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import  UpdateView

from django.shortcuts import redirect, render
from requests import request

from adv.forms import AdvForm
from adv.models import Adv
from contact.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.models import User



def index(request):
    # winer = Chance.objects.first()
    return render(request, 'index/index.html')

class LoginView(TemplateView):
    template_name = "index/registration/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("profile"))
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)

class ProfilePage(TemplateView):
    template_name = "index/registration/profile.html"

    def dispatch(self,request,*args, **kwargs):
        user_adv = Adv.objects.filter(login = request.user.username)
        if request.user.is_authenticated == True:
            return render(request, self.template_name, {'user_adv': user_adv})
        else:
            return render(request, 'index/index.html')

class RegisterView(TemplateView):
    template_name = "index/registration/register.html"
    # index_template_name = "index/index.html"

    # mes = 'Пароли не совпадают'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            # phone = request.POST.get('phone')

            if User.objects.filter(username=username).exists():
                return render(request, self.template_name, {'mes1': "Пользователь с таким логином уже существует"})
            if User.objects.filter(email=email).exists():
                return render(request, self.template_name, {'mes1': "Данный email уже используется"})
            if len(username) < 6:
                return render(request, self.template_name, {'mes1': "Логин менее 6 символов"})

            if password == '' and password2 == '':
                return render(request, self.template_name, {'mes1': "Поле пароля не должно быть пустым"})

            if password == password2:
                User.objects.create_user(username, email ,password )
                return redirect(reverse("login"))
            else:
                return render(request, self.template_name, {'mes1': "Пароли не совпадают"})

        return render(request, self.template_name)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data =  {
                'name': form.cleaned_data['name'],
                'title': form.cleaned_data['title'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'art': form.cleaned_data['art'],
                'message': form.cleaned_data['message'],

            }
            html_body = render_to_string('index/appointment_email.html', data)
            msg = EmailMultiAlternatives(subject = 'title',to = ['zamax77@mail.ru'],  )
            msg.attach_alternative(html_body,'text/html')
            msg.send()
            form.save()
            # return redirect('/')
            return render(request, 'index/send_message_ok.html')

    else:
        form = ContactForm()
        return render(request, 'index/contact.html',{'form': form})


def delete_adv(request):

    searchEl = request.POST.get('adv_for_del', '')
    adv_for_del = Adv.objects.get(art=searchEl)
    # print(adv_for_del)
    adv_for_del.delete()
    return render(request, 'index/registration/del_adv_ok.html')



def delete_account(request):
    searchUser = request.user.username
    q = User.objects.get(username = searchUser)
    q.delete()

    return render(request, 'index/registration/del_account_ok.html')

def get_new_password(request):
    login_from_form = request.POST.get('user_login')
    user_email_from_form = request.POST.get('user_email')

    if User.objects.filter(username=login_from_form).exists() and User.objects.filter(email=user_email_from_form).exists():
        u = User.objects.get(username=login_from_form)
        # u = User.objects.get(username=login_from_form)
        # ------------------------генерация пароля символов---------------------------------------
        chars = 'abcdefghijklnopqrstuvwxyz1234567890'
        new_password = ''
        for i in range(5):
            new_password += random.choice(chars)

        # -----------------Установка нового пароля на пользователя---------------------------------
        u.set_password(new_password)
        u.save()
        # ------------------- -------------------------------------------------------------

        data = {}
        data['login'] = login_from_form
        data['email'] = user_email_from_form
        data['password'] =  new_password

        # ---------------------- отправка письма с новым паролем-------------------------------

        html_body = render_to_string('index/appointment1_email.html', data)
        msg = EmailMultiAlternatives(subject='Восстановление пароля', to=[user_email_from_form], )
        msg.attach_alternative(html_body, 'text/html')
        msg.send()
        return render(request, 'index/registration/new_password_ok.html', )

    else:
        return render(request, 'index/registration/login.html', {'mes': "Ошибка в логине или пароле, или пользователь не существует"})









