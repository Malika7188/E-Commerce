"""
ASGI config for malika_couture project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'malika_couture.settings')

application = get_asgi_application()