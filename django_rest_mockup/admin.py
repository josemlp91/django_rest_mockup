from __future__ import unicode_literals

from .models import *
from django.contrib import admin
from django.apps import apps

for model in apps.get_app_config('mockup').models.values():
    admin.site.register(model)
