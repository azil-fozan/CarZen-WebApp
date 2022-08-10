from BI.decorators import login_required
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^profile/(?P<user_id>\d+)/$', login_required(views.UserProfile.as_view())),
    url(r'^profile/$', login_required(views.UserProfile.as_view())),
    url(r'^edit_profile/$', login_required(views.EditProfile.as_view())),
]
