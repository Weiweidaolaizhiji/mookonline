from django.shortcuts import render, reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from apps.user.models import UserProfile
from apps.user.forms import LoginForm, RegisterForm


# Create your views here.
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, requtest):
        register_form = RegisterForm(requtest.POST)
        newuser = UserProfile()
        if register_form.is_valid():
            newuser.username = register_form.cleaned_data['mobile']
            newuser.password = register_form.cleaned_data['password']
            newuser.save()
            # user = authenticate(username=newuser.username, password=newuser.password)
            login(requtest, newuser)
            return HttpResponseRedirect(reverse('index'))
            # return render(requtest,'index.html')
        else:
            return render(requtest, 'register.html', {'register_form': register_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request, *args, **kwargs):
        '''
        :param request:
        :param args: 可变参数，解析元组
        :param kwargs: 解析字典
        :return:
        '''
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # form校验通过
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # return render(request,'index.html',{'msg':'ok'})
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '账号或密码错误！！！'})
        return render(request, 'login.html', {'login_form': login_form})
