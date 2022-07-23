import sys
import traceback
import io

from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from BI.constants import USER_ROLES_r
from BI.models import User
from BI.utilities import execute_read_query
from user_profiles.models import MechanicDetail


class UserProfile(View):
    def __init__(self):
        super(UserProfile, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):
        return super(UserProfile, self).dispatch(request, *args, **kwargs)

    def get_user_details(self, request, user_id) -> dict:
        user_details = {}
        user = User.objects.filter(id=user_id).first()
        if user and user.user_role == 1 or user_id == request.user.id:
            expertise = 'Not listed'
            if user.user_role == 1:
                mechanic_detail = MechanicDetail.objects.filter(user_id=user_id).first()
                if mechanic_detail:
                    expertise = mechanic_detail.expertise
            first_name = user.first_name if user.first_name else user.full_name.split()[0] if user.full_name else None
            last_name = user.last_name if user.last_name else ' '.join(user.full_name.split()[1:]) if user.full_name else None

            user_details = {
                'user_type': USER_ROLES_r.get(user.user_role, ''),
                'first_name': first_name,
                'last_name': last_name,
                'user_email': user.email,
                'mobile_num': user.phone_number,
                'address': user.address,
                'postal_code': '',
                'state': user.state,
                'occupation': user.occupation,
                'country': user.country,
                'State': 'Engine mechanic',
                'expertise': expertise,
                'over_all_rating': user.rating,
                'rem_over_all_rating': 5 - (user.rating if user.rating else 5),
                'own_profile': True if request.user.id == user_id else False,

                #sevice history:
                'work_catagory': 'Engine',
                'car_worked_on': 'Grande',
                'rating': 3,
            }
        return user_details

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id', request.user.id)
        context = {
            'page_headding': 'My Profile' if request.user.id == user_id else f'{request.user.get_user_full_name()}\'s Profile',
        }
        context.update(self.get_user_details(request, user_id=user_id))
        if not context.get('user_type', None):
            return HttpResponseNotFound("User not found!\n<a href='/welcome_page/'>Back Home</a>")
        return render(request, 'basic_profile.html', context)
    def post(self, request, *args, **kwargs):

        return JsonResponse(data={})