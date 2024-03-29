from BI.decorators import login_required
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^profile/(?P<user_id>\d+)/$', login_required(views.UserProfile.as_view())),
    url(r'^profile/$', login_required(views.UserProfile.as_view())),
    url(r'^edit_profile/$', login_required(views.EditProfile.as_view())),
    url(r'^profile_history/(?P<user_id>\d+)/$', login_required(views.ProfileHistory.as_view())),
    url(r'^profile_history/$', login_required(views.ProfileHistory.as_view())),
    url(r'^appointments/$', login_required(views.Appointments.as_view())),
]
