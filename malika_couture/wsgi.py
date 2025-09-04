"""
WSGI config for malika_couture project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'malika_couture.settings')

application = get_wsgi_application()