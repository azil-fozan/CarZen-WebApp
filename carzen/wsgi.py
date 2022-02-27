"""
WSGI config for carzen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys
import django
from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ubuntu/sites/prodsite/Inventorymanagement')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carzen.settings')

application = get_wsgi_application()

django.setup()