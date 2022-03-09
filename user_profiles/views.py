import sys
import traceback
import io

from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from BI.utilities import execute_read_query

class UserProfile(View):
    def __init__(self):
        super(UserProfile, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):
        return super(UserProfile, self).dispatch(request, *args, **kwargs)

    def get_user_details(self, request) -> dict:
        return {
            'user_type': 'Mechanic',
            'first_name': 'Arslan',
            'last_name': 'Arslam',
            'user_email': 'arslan@umt.edu.pk',
            'mobile_num': '+923001234567',
            'address': 'Kasur',
            'postal_code': '55050',
            'state': 'Punjab',
            'occupation': 'Engine mechanic',
            'country': 'Pakistan',
            'State': 'Engine mechanic',
            'expertise': 'Engine',

            'work_catagory': 'Engine',
            'car_worked_on': 'Grande',
            'rating': 3,
        }

    def get(self, request, *args, **kwargs):
        context = {
            'page_headding': 'UserProfile',
        }
        context.update(self.get_user_details(request))
        return render(request, 'basic_profile.html', context)
    def post(self, request, *args, **kwargs):

        return JsonResponse(data={})