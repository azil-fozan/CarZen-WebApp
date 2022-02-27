"""
ASGI config for carzen project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import sys
import django
from django.core.asgi import get_asgi_application

sys.path.append('/home/ubuntu/sites/prodsite/Inventorymanagement')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carzen.settings')
django.setup()
application = get_asgi_application()
