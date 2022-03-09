from BI.decorators import login_required
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^receipts/$', views.UserProfile.as_view()),
]