import os
from os.path import exists
import sys
import traceback
import io

from django.db.models import Q
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.core.files.storage import FileSystemStorage
import uuid

from BI import settings
from BI.constants import USER_ROLES_r, ALLOWED_IMAGE_TYPES, IMAGE_MIME_TYPES, TOTAL_RATING
from BI.models import User
from BI.utilities import execute_read_query
from user_dashboards.constants import GENERAL_DATETIME_FORMAT, GENERAL_DATE
from user_profiles.models import MechanicDetail, ServiceHistory


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
                'user_id': user.pk,
                'first_name': first_name,
                'last_name': last_name,
                'full_name': f'{first_name} {last_name}',
                'user_email': user.email,
                'mobile_num': user.phone_number,
                'address': user.address,
                'postal_code': '',
                'state': user.state,
                'occupation': user.occupation,
                'country': user.country,
                'State': 'Engine mechanic',
                'expertise': expertise,

                'image': user.image,
                'over_all_rating': user.rating,
                'rem_over_all_rating': 5 - (user.rating if user.rating else 5),
                'own_profile': True if request.user.id == user_id else False,

                #sevice history:
                'work_catagory': 'Engine',
                'car_worked_on': 'Grande',
                'rating': 3,
            }
        return user_details


    def get_user_history(self, request, user_id) -> dict:
        service_history = {}
        history = []
        user = User.objects.filter(id=user_id).first()
        if user and user.user_role == 1 or user_id == request.user.id:
            if user.user_role == 1:
                service_hist = ServiceHistory.objects.filter(mech_id=user_id).order_by('-created_on')[:3]
                for hist in service_hist:
                    history.append({
                        'cat': hist.catagory,
                        'car': hist.car,
                        'rat': hist.rating,
                        'rem_rat': TOTAL_RATING - hist.rating,
                        'comments': hist.comments,
                    })

            service_history = {
                'service_history': history
            }
        return service_history

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id', request.user.id)
        context = {
            'page_headding': 'My Profile' if request.user.id == user_id else f'{User.objects.filter(pk=user_id).first().get_user_full_name()}\'s Profile',
        }

        context.update(self.get_user_details(request, user_id=user_id))
        context.update(self.get_user_history(request, user_id=user_id))

        if not context.get('user_type', None):
            return HttpResponseNotFound("User not found!\n<a href='/welcome_page/'>Back Home</a>")
        return render(request, 'basic_profile.html', context)

    def post(self, request, *args, **kwargs):

        return JsonResponse(data={})


class EditProfile(View):
    def __init__(self):
        super(EditProfile, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):
        return super(EditProfile, self).dispatch(request, *args, **kwargs)

    @staticmethod
    def upload_image(myfile):
        try:
            file_name = uuid.uuid4().hex
            fs = FileSystemStorage()
            filename = fs.save(f'{file_name}.{myfile.content_type.split("/")[-1]}', myfile)
            uploaded_file_url = fs.url(filename)
            return uploaded_file_url
        except:
            return None

    def post(self, request, *args, **kwargs):
        user_id = int(request.POST.get('user_id', 0))
        # full_name = request.POST.get('full_name')
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Occupation = request.POST.get('Occupation')
        country = request.POST.get('country')
        state = request.POST.get('state')

        new_user_image = request.FILES.get('image', None)
        user_obj = User.objects.filter(pk=user_id).first()
        if user_obj:
            user_obj.first_name = f_name
            user_obj.last_name = l_name
            user_obj.full_name = f'{f_name} {l_name}'
            user_obj.phone_number = phone
            user_obj.address = address
            user_obj.occupation = Occupation
            user_obj.country = country
            user_obj.state = state
            if new_user_image:
                # file_read = new_user_image.read()  # get binary data of image

                name, extension = os.path.splitext(new_user_image.name)
                extension = extension.lower()
                if extension not in ALLOWED_IMAGE_TYPES or new_user_image.content_type != IMAGE_MIME_TYPES[extension]:
                    return JsonResponse(data={'success': False, 'message': 'Not a valid file type'})
                new_file_url = EditProfile.upload_image(new_user_image)
                if new_file_url:
                    old_image = user_obj.image
                    try:
                        path_to_old_file = os.path.join(settings.MEDIA_ROOT, old_image.split('/')[-1])
                        if exists(path_to_old_file):
                            os.remove(path_to_old_file)
                    except:
                        pass
                    user_obj.image = new_file_url
                    self.response_data['new_file_url'] = new_file_url
            user_obj.save()
            self.response_data['message'] = 'Profie updated successfully!'
            self.response_data['success'] = True
        else:
            self.response_data['message'] = 'User does not exist!'
        return JsonResponse(data=self.response_data)


class ProfileHistory(View):
    def __init__(self):
        super(ProfileHistory, self).__init__()
        self.response_data = {'success': False}

    def dispatch(self, request, *args, **kwargs):
        return super(ProfileHistory, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        my_profile = True
        if user_id:
            my_profile = False
        else:
            user_id = request.user.id
        if not user_id:
            self.response_data['message'] = 'User Does not exist!'
            return JsonResponse(data=self.response_data)

        context = {
            'page_headding': 'Service History',
            'my_profile': my_profile,
            'user_full_name': User.objects.filter(pk=user_id).first().get_user_full_name(),
            'services': [],
        }
        return render(request, 'service_listing.html', context)

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        my_profile = True
        if user_id:
            my_profile = False
        else:
            user_id = request.user.id

        search_str = request.POST.get('search_str')
        if not user_id:
            self.response_data['message'] = 'User Does not exist!'
            return JsonResponse(data=self.response_data)
        if my_profile:
            service_history = ServiceHistory.objects.filter(Q(owner_id=user_id)|Q(mech_id=user_id))
        else:
            service_history = ServiceHistory.objects.filter(mech_id=user_id, status='Closed')
        if search_str:
            service_history = service_history.filter(Q(catagory__icontains=search_str) | Q(car__icontains=search_str))

        service_history = service_history.order_by('-status', '-created_on')

        service_history = service_history.values('pk', 'catagory', 'car', 'rating', 'status', 'comments', 'created_on')
        for _ in service_history:
            _.update({'created_on': _['created_on'].strftime(GENERAL_DATETIME_FORMAT),
                      'rem_rating': TOTAL_RATING - _['rating']})

        self.response_data.update({
            'table_rows_html': render_to_string('service_table_rows.html', context={'services': list(service_history)}),
            'success': True
        })
        return JsonResponse(data=self.response_data)

