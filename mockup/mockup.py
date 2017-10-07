# coding=utf-8
from __future__ import unicode_literals

import json

import requests

from recadvisor.apps.mockup.models import MockupConfig
from recadvisor.settings import BASE_DIR, MOCKUP_CREATE_DOMAIN


class MockupException(Exception): pass

class Mockup(object):
    """
    Clase encargada de gestionar Mockup REST.
    """
    def __init__(self):
        self.domain = MOCKUP_CREATE_DOMAIN


    def load_config(self):
        """Carga configuración desde un archivo JSON"""
        pass

    def get_mockup(self, view_name):
        return MockupConfig.objects.filter(name=view_name).first()


    def mockup_all_views(self):
        all_mockup_config = MockupConfig.objects.all()
        for mockup_config_item in all_mockup_config:
            self.create_mockup(mockup_config_item)

    def create_mockup(self, mockup_config):
        """
        Genera archivo Mockup dada la configuración de una vista.
        :param mockup_config: Configuración de una vista.
        :return:
        """
        response = None
        domain = self.domain
        url = domain + mockup_config.url
        method = mockup_config.method

        # Carga parametros formato payload
        get_param = {}
        if mockup_config.get_param:
            get_param = json.loads(mockup_config.get_param)

        # Parametros por url
        if mockup_config.url_param:
            params = mockup_config.url_param
            for param in params:
                url += "{0}/".format(param)

        # Parámetros tipo data
        data = {}
        if mockup_config.post_body_param:
            data = json.loads(mockup_config.post_body_param)

        print url

        if method == "GET":
            response = requests.get(url, params=get_param)
        elif method == "POST":
            response = requests.get(url, params=get_param, data=data)
        elif method == "PUT":
            response = requests.put(url, params=get_param, data=data)
        elif method == "DELETE":
            response = requests.delete(url, params=get_param, data=data)
        else:
            raise MockupException("Método HTTP no válido: {0}".format(method))

        if response:
            if response.status_code == requests.codes.ok:
                mockup_config.content = json.loads(response.content)
                mockup_config.save()
            else:
                print "Error en la peticion"
                raise MockupException("Imposible llamar al endpoint {0}, con el método {1}".format(url, method))






