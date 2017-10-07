# coding=utf-8
from __future__ import unicode_literals

import time
from django.core.management.base import BaseCommand

from recadvisor.settings import BASE_DIR, MOCKUP_CREATE_DOMAIN, ENABLE_MOCKUP_VIEWS

from recadvisor.apps.mockup.mockup import Mockup
from recadvisor.apps.tecdoc.models import ManufacturesManager, ModelSeriesManager, VehiclesManager
from recadvisor.settings import DEBUG

import django.conf as conf

class Command(BaseCommand):
	help = "Genera mockups de todas las vistas que tengan la configuración para ello."

	def handle(self, *args, **options):

		conf.settings.DATABASES['ENABLE_MOCKUP_VIEWS'] = False

		self.stdout.write(self.help)
		ma = Mockup()
		ma.mockup_all_views()
