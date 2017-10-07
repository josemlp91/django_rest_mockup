# coding=utf-8
from django.db import models
from jsonfield import JSONField


class MockupConfig(models.Model):
    HTTP_METHOD = (
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('PATH', 'PATH'),
        ('DELETE', 'DELET'),
    )

    name = models.CharField(max_length=1024, blank=False, null=False, verbose_name=u"nombre")
    url = models.CharField(max_length=1024, verbose_name=u"url", blank=False, null=False)
    method = models.CharField(max_length=1024, choices=HTTP_METHOD, null=False, blank=False, verbose_name=u"metodo http")
    url_param = JSONField(null=True, blank=True, verbose_name=u"parámetros por url")
    get_param = JSONField(null=True, blank=True, verbose_name=u"parámetros get")
    post_body_param = JSONField(null=True, blank=True, verbose_name=u"parámetros post")
    content = JSONField(null=True, blank=True, verbose_name=u"contenido")

    def __str__(self):
        return self.name
