<<<<<<< HEAD
=======
"""
WSGI config for vehicle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

>>>>>>> origin/main
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vehicle.settings')

application = get_wsgi_application()
<<<<<<< HEAD
=======

>>>>>>> origin/main
app = application
