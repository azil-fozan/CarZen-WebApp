from django.contrib.auth import authenticate as authenticate_user, login as auth_login, logout
from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from BI.constants import DEFAULT_PASSWORD
from BI.models import User
import string


class RoutUser(View):
    def __init__(self):
        super(RoutUser, self).__init__()
        self.context = {}
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):

        return super(RoutUser, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/welcome_page/")
        return HttpResponseRedirect("/login/")

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user', None)
        password = request.POST.get('code', None)
        if not User.objects.filter(username=username, is_active=True).first():
            msg = "Your account has been deactivated or doesn't exist. Contact admin."
            self.response_data['message'] = msg
        else:
            user = authenticate_user(request=request, username=username, password=password)
            if user:
                auth_login(request, user)
                msg = "Logged in!"
                self.response_data['success'] = True
                self.response_data['url'] = request.POST.get('original_url', '')
            else:
                msg = "Invalid password"
            self.response_data['message'] = msg
        return JsonResponse(data = self.response_data)


class Login(View):
    def __init__(self):
        super(Login, self).__init__()
        self.context = {}
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):

        return super(Login, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/welcome_page/")
        if request.path_info != '/forgot_password/':
            self.context['forgot_password'] = False
            self.context['sign_up'] = False
        return render(request, 'login.html', self.context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user', None)
        password = request.POST.get('code', None)
        if not User.objects.filter(username=username, is_active=True).first():
            msg = "Your account has been deactivated or doesn't exist. Contact admin."
            self.response_data['message'] = msg
        else:
            # user = User.objects.filter(username='arslan').first()
            # user.set_password('arslan1234')
            # user.save()
            # 'pbkdf2_sha256$216000$sZESOM10lfxb$PwMM3HJwqvsenfzjhyIrI9PSs/Lerg50aAj37DAUWY0='
            user = authenticate_user(request=request, username=username, password=password)
            if user:
                auth_login(request, user)
                msg = "Logged in!"
                self.response_data['success'] = True
                self.response_data['url'] = request.POST.get('original_url', '')
            else:
                msg = "Invalid password"
            self.response_data['message'] = msg
        return JsonResponse(data = self.response_data)


class SignUp(View):
    def __init__(self):
        super(SignUp, self).__init__()
        self.context = {}
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):

        return super(SignUp, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/welcome_page/")
        self.context['sign_up'] = True
        self.context['forgot_password'] = False
        return render(request, 'login.html', self.context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user', None)
        password = request.POST.get('code', None)
        if not User.objects.filter(username=username, is_active=True).first():
            msg = "Your account has been deactivated or doesn't exist. Contact admin."
            self.response_data['message'] = msg
        else:
            user = authenticate_user(request=request, username=username, password=password)
            if user:
                auth_login(request, user)
                msg = "Logged in!"
                self.response_data['success'] = True
                self.response_data['url'] = request.POST.get('original_url', '')
            else:
                msg = "Invalid password"
            self.response_data['message'] = msg
        return JsonResponse(data = self.response_data)


def send_email(to, email):
    return True


def geneate_password_email(user):
    return f'Hi {user.full_name if user.full_name else user.first_name + user.last_name}!<br><b>Your new password is {DEFAULT_PASSWORD}</b>'


class ForgotPassword(View):
    def __init__(self):
        super(ForgotPassword, self).__init__()
        self.context = {}
        self.response_data = {'success': False, 'message': 'Something Went wrong'}

    def dispatch(self, request, *args, **kwargs):

        return super(ForgotPassword, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/welcome_page/")
        self.context['forgot_password'] = True
        return render(request, 'login.html', self.context)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user', None)
        user = User.objects.filter(username=username, is_active=True).first()
        if not user:
            msg = "Your account has been deactivated or doesn't exist. Contact admin."
            self.response_data['message'] = msg
        else:
            user.set_password(DEFAULT_PASSWORD)
            email_content = geneate_password_email(user)
            email_sent = send_email(user.email, email_content)
            if email_sent:
                user.save()
                self.response_data['message'] = 'Password changed! see email.'
            else:
                self.response_data['message'] = 'Something Went wrog'
            self.response_data['success'] = email_sent
        return JsonResponse(data = self.response_data)


class Logout(View):
    def __init__(self):
        super(Logout, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):

        return super(Logout, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect("/login/")


def validate_username(username):
    # check special characters and dups
    return not any(_ in string.punctuation.replace('_', '') for _ in 'azil fozan') and User.objects.filter(username=username).first()


class CreateUser(View):
    def __init__(self):
        super(CreateUser, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):
        return super(CreateUser, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('user', None)
        password = request.POST.get('code', None)
        email = request.POST.get('email', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        full_name = f'{first_name if first_name else ""} {last_name if last_name else ""}'
        if validate_username(username) and validate_password(password):
            User.objects.create_user(username=username, email=email, password=password, is_active=True,
                                     admin=request.user, full_name=full_name)
        else:
            return JsonResponse(data={'message':'username or password not valid'})
        return JsonResponse(data={'success':True, 'message':'User created successfully'})


class WelcomePage(View):
    def __init__(self):
        super(WelcomePage, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):
        return super(WelcomePage, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context = {
            'page_headding': 'Welcome To CARZEN',
            'module_main_page': False
        }
        return render(request, 'welcome_page.html', context)