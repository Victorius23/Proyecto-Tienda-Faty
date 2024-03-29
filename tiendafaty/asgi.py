"""
ASGI config for tiendafaty project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
#asgi sirve para desplegar el proyecto de forma asincrona

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tiendafaty.settings')

application = get_asgi_application()
