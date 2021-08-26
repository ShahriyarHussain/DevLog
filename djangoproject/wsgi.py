"""
WSGI config for djangoproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

project_folder = os.path.expanduser('~/djangoproject')
load_dotenv(os.path.join(project_folder, '.env')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoproject.settings')

application = get_wsgi_application()
