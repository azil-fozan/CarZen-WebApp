"""CARZEN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.static import serve
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import re_path, include, path
from BI import views, settings
from BI.decorators import login_required

urlpatterns = [
    re_path(r'^$', views.Login.as_view()),
    re_path(r'^login/$', views.Login.as_view()),
    re_path(r'^signup/$', views.SignUp.as_view()),
    re_path(r'^forgot_password/$', views.ForgotPassword.as_view()),
    re_path(r'^logout/$', views.Logout.as_view()),
    re_path(r'^welcome_page/$', login_required(views.WelcomePage.as_view())),
    # re_path(r'^create_user/$', views.CreateUser.as_view()),
    path(r'dashboards/', include(('user_dashboards.urls', 'user_dashboards'), namespace='user_dashboards')),
    path(r'user_profile/', include(('user_profiles.urls', 'user_profiles'), namespace='user_profiles')),

    # for heroku deployment!
    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('admin/', admin.site.urls),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
